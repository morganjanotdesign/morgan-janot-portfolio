# encoding: UTF-8
require "json"

# Helper to compute bounding box from path d
def get_bbox(d)
  pts = []
  d.scan(/([MLC])\s*([^MLCZ]+)/).each do |cmd, coords|
    nums = coords.scan(/[-+]?\d*\.?\d+/).map(&:to_f)
    nums.each_slice(2) do |x, y|
      pts << [x, y] if x && y
    end
  end
  min_x = pts.map(&:first).min
  max_x = pts.map(&:first).max
  min_y = pts.map(&:last).min
  max_y = pts.map(&:last).max
  [min_x, min_y, max_x, max_y, max_x - min_x, max_y - min_y]
end

# Normalize path to (0, 0)
def normalize_path(d, ox, oy)
  # Replace all coordinates by subtracting ox, oy
  # We parse token by token
  tokens = d.scan(/[MLCZ]|[-+]?\d*\.?\d+/)
  res = []
  i = 0
  while i < tokens.length
    tok = tokens[i]
    if tok =~ /^[MLCZ]$/
      res << tok
      i += 1
    else
      x = tok.to_f - ox
      y = tokens[i+1].to_f - oy
      res << "#{x.round(2)} #{y.round(2)}"
      i += 2
    end
  end
  res.join(" ")
end

keys = ["tile1_orange", "tile2_purple", "tile3_green", "tile4_brown", "tile5_blue", "mj_black"]
vector_data = {}

keys.each do |k|
  d = File.read("/Users/morganjanot/.gemini/antigravity/scratch/#{k}_d.txt").strip
  min_x, min_y, max_x, max_y, w, h = get_bbox(d)
  puts "#{k}: bbox x=[#{min_x.round(1)}..#{max_x.round(1)}] (w=#{w.round(1)}), y=[#{min_y.round(1)}..#{max_y.round(1)}] (h=#{h.round(1)})"
  
  # Normalize to origin (0, 0) with a clean viewBox
  norm_d = normalize_path(d, min_x, min_y)
  vector_data[k] = {
    "d" => norm_d,
    "width" => w.round(2),
    "height" => h.round(2),
    "viewBox" => "0 0 #{w.ceil} #{h.ceil}"
  }

  # Write test SVG
  stroke_attr = k == "mj_black" ? "fill=\"#000\"" : "fill=\"none\" stroke=\"currentColor\" stroke-width=\"4\" stroke-linecap=\"round\" stroke-linejoin=\"round\""
  svg = <<~SVG
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 #{w.ceil + 10} #{h.ceil + 10}" width="#{w.ceil}" height="#{h.ceil}">
      <g transform="translate(5, 5)">
        <path #{stroke_attr} d="#{norm_d}" />
      </g>
    </svg>
  SVG
  File.write("/Users/morganjanot/.gemini/antigravity/scratch/#{k}.svg", svg)
end

File.write("/Users/morganjanot/.gemini/antigravity/scratch/normalized_vectors.json", JSON.pretty_generate(vector_data))
puts "Successfully normalized all 6 vectors!"
