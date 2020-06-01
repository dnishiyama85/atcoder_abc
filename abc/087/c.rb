n = gets.to_i
as = []
as << gets.strip.split.map(&:to_i)
as << gets.strip.split.map(&:to_i)

mx = 0

for i in (0...n)
  # i番目のマスで下に移動することにした場合
  upper = as[0][0..i].inject(:+)
  lower = as[1][i..-1].inject(:+)
  mx = [upper + lower, mx].max
end

puts mx
