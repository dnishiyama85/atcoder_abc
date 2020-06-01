t = gets.to_i
n = gets.to_i
as = gets.strip.split.map(&:to_i)
m = gets.to_i
bs = gets.strip.split.map(&:to_i)

def tako(t, takoyakis, guests)
  return true if guests.empty?
  return false if takoyakis.empty?
  g = guests.shift
  tak = takoyakis.shift
  return false if g < tak || tak + t < g
  tako t, takoyakis, guests
end

is_success = tako t, as, bs

if is_success
  puts 'yes'
else
  puts 'no'
end
