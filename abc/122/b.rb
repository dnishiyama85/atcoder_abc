s = gets.strip

b = -1
e = -1

max = 0

while true do
    if e == s.size - 1
        break
    end
    e += 1
    if 'ACGT'.include? s[e]
        max = [max, e - b].max
    else
        b = e
    end
end

puts max

