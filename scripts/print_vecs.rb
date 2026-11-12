require "json"
vecs = JSON.parse(File.read("/Users/morganjanot/.gemini/antigravity/scratch/normalized_vectors.json"))
vecs.each do |k, v|
  puts "#{k}: viewBox #{v['viewBox']}, width=#{v['width']}, height=#{v['height']}"
end
