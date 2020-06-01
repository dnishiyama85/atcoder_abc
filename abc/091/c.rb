n = gets.to_i
reds = []
blues = []
n.times do
  reds << gets.strip.split.map(&:to_i)
end
n.times do
  blues << gets.strip.split.map(&:to_i)
end

blues.sort_by! { |p| - p[0].abs - p[1].abs }
reds.sort_by!  { |p| - p[0].abs - p[1].abs }

count = 0
blues.each do |pb|
  a, b = pb
  paired = reds.each_with_index.select do |pr, ind|
    c, d = pr
    c < a && d < b
  end
  if !paired.nil? && !paired.empty?
    index = paired.min do |a, b|
      ax, ay = a[0]
      bx, by = b[0]
      (ax - bx).abs + (ay - by).abs
    end
    count += 1
    reds.delete_at index[1]
  end
end

puts count
