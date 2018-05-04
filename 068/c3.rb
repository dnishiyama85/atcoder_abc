n, m = gets.strip.split.map(&:to_i)
graph = {}
m.times do
  a, b = gets.strip.split.map(&:to_i)
  if a == 1 || b == 1 || a == n || b == n
    graph[a].nil? ? graph[a] = [b] : graph[a] << b
    graph[b].nil? ? graph[b] = [a] : graph[b] << a
  end
end

(1..n).each do |i|
  edges = graph[i]
  if edges && edges.include?(1) && edges.include?(n)
    puts "POSSIBLE"
    exit 0
  end
end

puts "IMPOSSIBLE"
