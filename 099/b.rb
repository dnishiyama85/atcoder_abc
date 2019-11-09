a, b = gets.strip.split.map(&:to_i)

for i in 1..999
    h1 = i * (i + 1) / 2
    h2 = (i + 1) * (i + 2) / 2
    if h1 - a == h2 - b
        puts (h1 - a)
        break
    end
end

