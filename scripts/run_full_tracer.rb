require "zlib"

data = File.binread("/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/.user_uploaded/media_1790627723925.png")
pos = 8; idat = ""; w = 0; h = 0
while pos < data.length
  len = data[pos, 4].unpack1("N"); type = data[pos+4, 4]; chunk = data[pos+8, len]
  w, h = chunk[0, 8].unpack("NN") if type == "IHDR"
  idat << chunk if type == "IDAT"
  break if type == "IEND"
  pos += 12 + len
end
raw = Zlib::Inflate.inflate(idat); bpp = 4; stride = 1 + w * bpp
img = Array.new(h) { Array.new(w) }
prev_line = Array.new(w * bpp, 0)
h.times do |y|
  filter = raw[y * stride].ord; curr_line = raw[y * stride + 1, w * bpp].bytes
  case filter
  when 1; (bpp...(w*bpp)).each { |i| curr_line[i] = (curr_line[i] + curr_line[i-bpp]) & 0xFF }
  when 2; (0...(w*bpp)).each { |i| curr_line[i] = (curr_line[i] + prev_line[i]) & 0xFF }
  when 3; (0...(w*bpp)).each { |i| curr_line[i] = (curr_line[i] + ((curr_line[i-bpp] + prev_line[i]) / 2)) & 0xFF }
  when 4; (0...(w*bpp)).each { |i|
      a = i >= bpp ? curr_line[i-bpp] : 0; b = prev_line[i]; c = i >= bpp ? prev_line[i-bpp] : 0
      p = a + b - c; pa = (p - a).abs; pb = (p - b).abs; pc = (p - c).abs
      pr = (pa <= pb && pa <= pc) ? a : ((pb <= pc) ? b : c)
      curr_line[i] = (curr_line[i] + pr) & 0xFF
    }
  end
  prev_line = curr_line
  w.times { |x| img[y][x] = [curr_line[x*bpp], curr_line[x*bpp + 1], curr_line[x*bpp + 2]] }
end

def perpendicular_distance(pt, line_start, line_end)
  dx = line_end[0] - line_start[0]
  dy = line_end[1] - line_start[1]
  mag = Math.hypot(dx, dy)
  return Math.hypot(pt[0] - line_start[0], pt[1] - line_start[1]) if mag == 0
  ((dy * pt[0] - dx * pt[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0]).abs) / mag
end

def rdp(points, epsilon)
  return points if points.length <= 2
  dmax = 0.0
  index = 0
  (1...(points.length - 1)).each do |i|
    d = perpendicular_distance(points[i], points[0], points[-1])
    if d > dmax
      index = i
      dmax = d
    end
  end
  if dmax > epsilon
    rec1 = rdp(points[0..index], epsilon)
    rec2 = rdp(points[index..-1], epsilon)
    rec1[0...-1] + rec2
  else
    [points[0], points[-1]]
  end
end

def trace_mask_to_paths(mask, width, height, epsilon = 1.0)
  adj = Hash.new { |h, k| h[k] = [] }
  height.times do |y|
    width.times do |x|
      next unless mask[y][x] == 1
      adj[[x, y]] << [x + 1, y] if y == 0 || mask[y - 1][x] == 0
      adj[[x + 1, y]] << [x + 1, y + 1] if x == width - 1 || mask[y][x + 1] == 0
      adj[[x + 1, y + 1]] << [x, y + 1] if y == height - 1 || mask[y + 1][x] == 0
      adj[[x, y + 1]] << [x, y] if x == 0 || mask[y][x - 1] == 0
    end
  end

  loops = []
  while (start_v = adj.keys.find { |k| !adj[k].empty? })
    curr_v = start_v
    loop_pts = [curr_v]
    while (next_v = adj[curr_v].pop)
      adj.delete(curr_v) if adj[curr_v].empty?
      curr_v = next_v
      break if curr_v == start_v
      loop_pts << curr_v
    end
    adj.delete(start_v) if adj[start_v]&.empty?
    if loop_pts.length > 8
      loop_pts << loop_pts.first
      simp = rdp(loop_pts, epsilon)
      loops << simp if simp.length >= 3
    end
  end
  loops
end

def loops_to_svg_d(loops, offset_x = 0, offset_y = 0)
  d = []
  loops.each do |lp|
    first = lp.first
    path_str = "M #{(first[0] - offset_x).round(1)} #{(first[1] - offset_y).round(1)} "
    lp[1..-1].each do |pt|
      path_str << "L #{(pt[0] - offset_x).round(1)} #{(pt[1] - offset_y).round(1)} "
    end
    path_str << "Z"
    d << path_str
  end
  d.join(" ")
end

tiles_info = [
  { id: 1, name: "tile1", x0: 0, x1: 439, y0: 0, y1: 339, bg: [233, 114, 43], stroke_color: "#eb6209" },
  { id: 2, name: "tile2", x0: 440, x1: 878, y0: 0, y1: 339, bg: [145, 71, 146], stroke_color: "#812383" },
  { id: 3, name: "tile3", x0: 0, x1: 439, y0: 340, y1: 681, bg: [104, 180, 45], stroke_color: "#2c8934" },
  { id: 4, name: "tile4", x0: 440, x1: 878, y0: 340, y1: 681, bg: [119, 87, 50], stroke_color: "#724b10" },
  { id: 5, name: "tile5", x0: 0, x1: 439, y0: 682, y1: 1023, bg: [70, 160, 209], stroke_color: "#27629f" }
]

out_dir = "/Users/morganjanot/.gemini/antigravity/scratch/extracted_svgs"
Dir.mkdir(out_dir) unless Dir.exist?(out_dir)

tiles_info.each do |ti|
  tw = ti[:x1] - ti[:x0] + 1
  th = ti[:y1] - ti[:y0] + 1
  mask_main = Array.new(th) { Array.new(tw, 0) }
  mask_arrow = Array.new(th) { Array.new(tw, 0) }

  th.times do |local_y|
    global_y = ti[:y0] + local_y
    tw.times do |local_x|
      global_x = ti[:x0] + local_x
      # ignore MJ logo and About/Contact in top row
      next if global_y < 85 && (global_x > 350 || (ti[:id] == 2 && global_x > 650))
      
      rgb = img[global_y][global_x]
      diff = (rgb[0] - ti[:bg][0]).abs + (rgb[1] - ti[:bg][1]).abs + (rgb[2] - ti[:bg][2]).abs
      if diff > 32
        # Check if pixel belongs to arrow:
        # Arrow criteria for each tile:
        is_arrow = false
        case ti[:id]
        when 1
          # Tile 1 arrow is at bottom right: x > 310, y > 240
          is_arrow = true if local_x > 310 && local_y > 240
        when 2
          # Tile 2 arrow is at x > 250 (global x > 690), y > 240
          is_arrow = true if local_x > 250 && local_y > 240
        when 3
          # Tile 3 arrow is at x > 260, y > 240
          is_arrow = true if local_x > 260 && local_y > 240
        when 4
          # Tile 4 arrow is at x > 260, y > 240
          is_arrow = true if local_x > 260 && local_y > 240
        when 5
          # Tile 5 arrow is at x > 260, y > 230
          is_arrow = true if local_x > 260 && local_y > 230
        end

        if is_arrow
          mask_arrow[local_y][local_x] = 1
        else
          mask_main[local_y][local_x] = 1
        end
      end
    end
  end

  main_loops = trace_mask_to_paths(mask_main, tw, th, 1.2)
  arrow_loops = trace_mask_to_paths(mask_arrow, tw, th, 1.2)

  main_d = loops_to_svg_d(main_loops)
  arrow_d = loops_to_svg_d(arrow_loops)

  puts "Tile #{ti[:id]}: main loops=#{main_loops.size}, arrow loops=#{arrow_loops.size}"

  # Write standalone SVG
  svg_content = <<~SVG
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 #{tw} #{th}" width="#{tw}" height="#{th}" style="background-color: #{'#%02x%02x%02x' % ti[:bg]};">
      <path fill="#{ti[:stroke_color]}" fill-rule="evenodd" d="#{main_d}" />
      <path fill="#{ti[:stroke_color]}" fill-rule="evenodd" d="#{arrow_d}" />
    </svg>
  SVG
  File.write("#{out_dir}/#{ti[:name]}.svg", svg_content)
  File.write("#{out_dir}/#{ti[:name]}_main_d.txt", main_d)
  File.write("#{out_dir}/#{ti[:name]}_arrow_d.txt", arrow_d)
end

puts "Extraction complete!"
