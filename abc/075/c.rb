def bfs(graph, start, rm)
  visited = {}
  count = 0
  queue = [start]
  until queue.empty? do
    p = queue.shift
    neighbors = graph[p]
    neighbors.each do |n|
      next if visited[n]
      next if (p == rm[0] && n == rm[1]) || (p == rm[1] && n == rm[0])
      visited[n] = true
      queue.push(n)
      count += 1
    end
  end
  count
end

@visited = {}
@count = 0
def dfs(graph, now, rm)
  @visited[now] = true
  @count += 1
  neighbors = graph[now]
  neighbors.each do |n|
    next if @visited[n]
    next if (now == rm[0] && n == rm[1]) || (now == rm[1] && n == rm[0])
    dfs(graph, n, rm)
  end
end

n, m = gets.strip.split.map(&:to_i)
graph = {}
(1..n).each do |i|
  graph[i] = []
end

edges = []
m.times do
  a, b = gets.strip.split.map(&:to_i)
  graph[a] << b
  graph[b] << a
  edges << [a, b]
end

num_bridges = 0
edges.each do |e|
  @visited = {}
  @count = 0
  dfs(graph, 1, e)
  #count = bfs(graph, 1, e)
  num_bridges += 1 if @count < n
end

puts num_bridges
