n = gets.to_i
as = gets.strip.split.map(&:to_i)
while as.size > 1 do
    min_a = as.min
    min_ind = as.index(min_a)
    for i in 0...as.size
        if i == min_ind
            next
        end
        as[i] %= min_a
    end
    as = as.select { |a| a > 0 }
    if as.size == 0
        break
    end
end

puts min_a

