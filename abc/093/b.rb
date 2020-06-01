a, b, k = gets.strip.split.map(&:to_i)

list = []

(1..k).each do |i|
  list << a + i - 1
  list << b - i + 1
end

sorted = list.select { |i| a <= i && i <= b }.uniq.sort

sorted.each do |i|
  puts i
end
