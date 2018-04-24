n = gets.to_i
as = gets.strip.split.map(&:to_i).sort

m = as.pop
r = as.map { |a| [a, (a - m / 2.0).abs] }.to_h.sort_by { |h| h[1] }[0][0]

puts "#{m} #{r}"
