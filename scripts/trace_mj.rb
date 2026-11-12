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
  dx = line_end[0] - line_start[0]; dy = line_end[1] - line_start[1]
  mag = Math.hypot(dx, dy)
  return Math.hypot(pt[0] - line_start[0], pt[1] - line_start[1]) if mag == 0
  ((dy * pt[0] - dx * pt[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0]).abs) / mag
end

def rdp(points, epsilon)
  return points if points.length <= 2
  dmax = 0.0; index = 0
  (1...(points.length - 1)).each do |i|
    d = perpendicular_distance(points[i], points[0], points[-1])
    if d > dmax; index = i; dmax = d; end
  end
  if dmax > epsilon
    rec1 = rdp(points[0..index], epsilon)
    rec2 = rdp(points[index..-1], epsilon)
    rec1[0...-1] + rec2
  else
    [points[0], points[-1]]
  end
end

def trace_mask_to_paths(mask, width, height, epsilon = 0.8)
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
    curr_v = start_v; loop_pts = [curr_v]
    while (next_v = adj[curr_v].pop)
      adj.delete(curr_v) if adj[curr_v].empty?
      curr_v = next_v
      break if curr_v == start_v
      loop_pts << curr_v
    end
    adj.delete(start_v) if adj[start_v]&.empty?
    
    xs = loop_pts.map(&:first); ys = loop_pts.map(&:last)
    bw = xs.max - xs.min; bh = ys.max - ys.min
    next if bw <= 1 && bh <= 1
    next if bw == 0 || bh == 0
    next if loop_pts.length < 8

    loop_pts << loop_pts.first
    simp = rdp(loop_pts, epsilon)
    loops << simp if simp.length >= 3
  end
  loops
end

def loops_to_svg_d(loops)
  d = []
  loops.each do |lp|
    first = lp.first
    path_str = "M #{first[0]} #{first[1]} "
    lp[1..-1].each { |pt| path_str << "L #{pt[0]} #{pt[1]} " }
    path_str << "Z"
    d << path_str
  end
  d.join(" ")
end

# Find exact bounds of MJ logo
mj_x0, mj_x1 = 370, 500
mj_y0, mj_y1 = 10, 85
mw = mj_x1 - mj_x0 + 1
mh = mj_y1 - mj_y0 + 1
mask = Array.new(mh) { Array.new(mw, 0) }

mh.times do |my|
  y = mj_y0 + my
  mw.times do |mx|
    x = mj_x0 + mx
    rgb = img[y][x]
    bg = x < 440 ? [233, 114, 43] : [145, 71, 146]
    diff = (rgb[0] - bg[0]).abs + (rgb[1] - bg[1]).abs + (rgb[2] - bg[2]).abs
    mask[my][mx] = 1 if diff > 50 && (rgb[0] + rgb[1] + rgb[2]) > 420
  end
end

mj_loops = trace_mask_to_paths(mask, mw, mh, 0.8)
mj_d = loops_to_svg_d(mj_loops)

out_dir = "/Users/morganjanot/.gemini/antigravity/scratch/extracted_svgs"
File.write("#{out_dir}/mj_logo_d.txt", mj_d)
svg_content = <<~SVG
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 #{mw} #{mh}" width="#{mw}" height="#{mh}">
    <path fill="currentColor" fill-rule="evenodd" d="#{mj_d}" />
  </svg>
SVG
File.write("#{out_dir}/mj_logo.svg", svg_content)
puts "MJ logo vectorized! Loops: #{mj_loops.size}, path length: #{mj_d.length}"
