words = []
n = gets.to_i
blues = []
n.times do
  s = gets.strip
  blues << s
  words << s
end

m = gets.to_i
reds = []
m.times do
  t = gets.strip
  reds << t
  words << t
end

mx = -10000000
words.sort.uniq.each do |w|
  plus = blues.count w
  minus = reds.count w
  mx = [mx, plus - minus].max
end

puts [mx, 0].max
