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

# Check pixels in Tile 2 for y in 0..85 and x in 440..660
hits = []
85.times do |y|
  (440..660).each do |x|
    # MJ logo is x <= 500
    next if x <= 500 && y <= 75
    rgb = img[y][x]
    diff = (rgb[0] - 145).abs + (rgb[1] - 71).abs + (rgb[2] - 146).abs
    hits << [x - 440, y] if diff > 30
  end
end
puts "Tile 2 top hits: #{hits.size} pixels found between y=0 and 85, x in 500..660"
