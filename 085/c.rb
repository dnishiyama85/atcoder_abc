n, y = gets.strip.split.map(&:to_i)

found = false
_i, _j, _k = -1, -1, -1
for i in 0..n
    break if found
    for j in 0..n-i
        k = n - i - j
        total = 10000 * i + 5000 * j + 1000 * k
        if total == y
            found = true
            _i, _j, _k = i, j, k
            break
        end
    end
end

puts "#{_i} #{_j} #{_k}"

