s = gets.strip
t = gets.strip

result = false
(s.size).times do
    if s == t
        result = true
        break
    end
    last = s[-1]
    s = last + s[0..-2]
end

puts result ? 'Yes' : 'No'

