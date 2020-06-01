require 'set'

n, m = gets.strip.split.map(&:to_i)
wars = []
m.times do
    wars << gets.strip.split.map(&:to_i)
end

# 橋がどの争いに巻き込まれているか
memo = []
(n).times do |i|
    memo << { begin: [], end: [] }
end

wars.each_with_index do |w, i|
    a, b = w
    memo[a - 1][:begin] << i
    memo[b - 1][:end] << i
end

bridges = []
set = Set.new()
memo.each_with_index do |m|
    m[:begin].each do |a|
        set.add(a)
    end
    m[:end].each do |b|
        set.delete(b)
    end
    bridges << set.clone
end

p bridges
