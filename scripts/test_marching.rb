# Ramer-Douglas-Peucker line simplification
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

puts "RDP test: #{rdp([[0,0], [1,0.1], [2,-0.1], [3,0]], 0.5).inspect}"
