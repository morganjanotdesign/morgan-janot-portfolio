# encoding: UTF-8
require "json"

content = File.read("/Users/morganjanot/.gemini/antigravity/scratch/page_stream.txt")
page_h = 1261.38

# Matrix helpers
# [a, b, c, d, e, f]
def identity_matrix
  [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
end

def multiply_matrix(m1, m2)
  a1, b1, c1, d1, e1, f1 = m1
  a2, b2, c2, d2, e2, f2 = m2
  [
    a1 * a2 + c1 * b2,
    b1 * a2 + d1 * b2,
    a1 * c2 + c1 * d2,
    b1 * c2 + d1 * d2,
    a1 * e2 + c1 * f2 + e1,
    b1 * e2 + d1 * f2 + f1
  ]
end

def apply_matrix(m, x, y)
  a, b, c, d, e, f = m
  [a * x + c * y + e, b * x + d * y + f]
end

# Split tokens
tokens = content.scan(/[^\s]+/)

matrix_stack = [identity_matrix]
current_matrix = identity_matrix

current_color = "none"
objects = {
  "tile2_purple" => [], # 0.606 0.986 0 0
  "tile1_orange" => [], # 0 0.72 1 0
  "tile3_green"  => [], # 0.8 0.21 1 0.08
  "tile4_brown"  => [], # 0.36 0.6 1 0.47
  "tile5_blue"   => [], # 0.87 0.59 0.12 0.01
  "mj_black"     => []  # 0.912 0.787 0.62 0.974
}

color_map = {
  "0.606 0.986 0 0" => "tile2_purple",
  "0 0.72 1 0" => "tile1_orange",
  "0.8 0.21 1 0.08" => "tile3_green",
  "0.36 0.6 1 0.47" => "tile4_brown",
  "0.87 0.59 0.12 0.01" => "tile5_blue",
  "0.912 0.787 0.62 0.974" => "mj_black"
}

i = 0
cur_x = 0.0
cur_y = 0.0
path_d = []
current_target = nil

# Colors can have 4 values before K or k
while i < tokens.length
  tok = tokens[i]
  
  case tok
  when "q"
    matrix_stack.push(current_matrix.dup)
    i += 1
  when "Q"
    current_matrix = matrix_stack.pop || identity_matrix
    i += 1
  when "cm"
    f = tokens[i-1].to_f
    e = tokens[i-2].to_f
    d = tokens[i-3].to_f
    c = tokens[i-4].to_f
    b = tokens[i-5].to_f
    a = tokens[i-6].to_f
    new_m = [a, b, c, d, e, f]
    current_matrix = multiply_matrix(current_matrix, new_m)
    i += 1
  when "K", "k"
    # 4 numbers before
    c_str = [tokens[i-4], tokens[i-3], tokens[i-2], tokens[i-1]].join(" ")
    if color_map[c_str]
      current_target = color_map[c_str]
      puts "Found target: #{current_target} at token #{i}"
    end
    i += 1
  when "m"
    x = tokens[i-2].to_f
    y = tokens[i-1].to_f
    gx, gy = apply_matrix(current_matrix, x, y)
    svg_y = page_h - gy
    cur_x = gx
    cur_y = gy
    path_d << "M #{gx.round(3)} #{svg_y.round(3)}"
    i += 1
  when "l"
    x = tokens[i-2].to_f
    y = tokens[i-1].to_f
    gx, gy = apply_matrix(current_matrix, x, y)
    svg_y = page_h - gy
    cur_x = gx
    cur_y = gy
    path_d << "L #{gx.round(3)} #{svg_y.round(3)}"
    i += 1
  when "c"
    x1 = tokens[i-6].to_f; y1 = tokens[i-5].to_f
    x2 = tokens[i-4].to_f; y2 = tokens[i-3].to_f
    x3 = tokens[i-2].to_f; y3 = tokens[i-1].to_f
    gx1, gy1 = apply_matrix(current_matrix, x1, y1)
    gx2, gy2 = apply_matrix(current_matrix, x2, y2)
    gx3, gy3 = apply_matrix(current_matrix, x3, y3)
    cur_x = gx3; cur_y = gy3
    path_d << "C #{gx1.round(3)} #{(page_h - gy1).round(3)}, #{gx2.round(3)} #{(page_h - gy2).round(3)}, #{gx3.round(3)} #{(page_h - gy3).round(3)}"
    i += 1
  when "v"
    # first control point is current point
    x2 = tokens[i-4].to_f; y2 = tokens[i-3].to_f
    x3 = tokens[i-2].to_f; y3 = tokens[i-1].to_f
    gx1 = cur_x; gy1 = cur_y
    gx2, gy2 = apply_matrix(current_matrix, x2, y2)
    gx3, gy3 = apply_matrix(current_matrix, x3, y3)
    cur_x = gx3; cur_y = gy3
    path_d << "C #{gx1.round(3)} #{(page_h - gy1).round(3)}, #{gx2.round(3)} #{(page_h - gy2).round(3)}, #{gx3.round(3)} #{(page_h - gy3).round(3)}"
    i += 1
  when "y"
    # second control point is final point
    x1 = tokens[i-4].to_f; y1 = tokens[i-3].to_f
    x3 = tokens[i-2].to_f; y3 = tokens[i-1].to_f
    gx1, gy1 = apply_matrix(current_matrix, x1, y1)
    gx3, gy3 = apply_matrix(current_matrix, x3, y3)
    gx2 = gx3; gy2 = gy3
    cur_x = gx3; cur_y = gy3
    path_d << "C #{gx1.round(3)} #{(page_h - gy1).round(3)}, #{gx2.round(3)} #{(page_h - gy2).round(3)}, #{gx3.round(3)} #{(page_h - gy3).round(3)}"
    i += 1
  when "h"
    path_d << "Z"
    i += 1
  when "S", "s", "f", "f*", "B", "b"
    if current_target && !path_d.empty?
      objects[current_target] << path_d.join(" ")
      path_d = []
    end
    i += 1
  else
    i += 1
  end
end

objects.each do |k, paths|
  full_d = paths.join(" ")
  puts "#{k}: #{paths.size} subpaths, total length #{full_d.length}"
  File.write("/Users/morganjanot/.gemini/antigravity/scratch/#{k}_d.txt", full_d)
end
