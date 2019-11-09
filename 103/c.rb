n = gets.to_i
as = gets.strip.split.map(&:to_i)

puts as.inject(:+) - n

