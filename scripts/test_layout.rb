# encoding: UTF-8
require "json"

vecs = JSON.parse(File.read("/Users/morganjanot/.gemini/antigravity/scratch/normalized_vectors.json"))

puts "All vector keys available: #{vecs.keys.inspect}"
