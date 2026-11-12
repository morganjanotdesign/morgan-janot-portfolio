def trace_mask_to_paths(mask, width, height, epsilon = 1.2)
  # Collect directed edges
  # edge map: start_pt -> [end_pt, ...]
  adj = Hash.new { |h, k| h[k] = [] }
  height.times do |y|
    width.times do |x|
      next unless mask[y][x] == 1
      # Top edge: (x, y) -> (x+1, y)
      adj[[x, y]] << [x + 1, y] if y == 0 || mask[y - 1][x] == 0
      # Right edge: (x+1, y) -> (x+1, y+1)
      adj[[x + 1, y]] << [x + 1, y + 1] if x == width - 1 || mask[y][x + 1] == 0
      # Bottom edge: (x+1, y+1) -> (x, y+1)
      adj[[x + 1, y + 1]] << [x, y + 1] if y == height - 1 || mask[y + 1][x] == 0
      # Left edge: (x, y+1) -> (x, y)
      adj[[x, y + 1]] << [x, y] if x == 0 || mask[y][x - 1] == 0
    end
  end

  # Now stitch edges into closed loops
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
    # Only keep loops with meaningful area/length (e.g. > 10 points)
    if loop_pts.length > 8
      # close the loop
      loop_pts << loop_pts.first
      # simplify with RDP
      simp = rdp(loop_pts, epsilon)
      loops << simp if simp.length >= 3
    end
  end
  loops
end

# RDP
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

puts "Trace setup defined successfully"
