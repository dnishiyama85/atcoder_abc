n = gets.to_i
as = gets.strip.split.map(&:to_i)
as.unshift(0)
as << 0

total = 0
for i in 0..n
  total += (as[i] - as[i + 1]).abs
end

(1..n).each do |i|
  c1 = (as[i - 1] - as[i]).abs + (as[i] - as[i + 1]).abs
  c2 = (as[i - 1] - as[i + 1]).abs
  puts (total - c1 + c2)
end
