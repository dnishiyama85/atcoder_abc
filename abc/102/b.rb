n = gets.to_i
as = gets.strip.split.map(&:to_i)

mx = 0
for a1 in as
    for a2 in as
        mx = [mx, (a1 - a2).abs].max
    end
end

puts mx

