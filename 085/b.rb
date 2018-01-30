n = gets.to_i

mochis = []

n.times do |i|
    mochis << gets.to_i
end

puts mochis.sort.uniq.size

