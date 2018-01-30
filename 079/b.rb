n = gets.to_i

@memo = {}
def lucas(n)
    if @memo[n]
        return @memo[n]
    end
    return 2 if n == 0
    return 1 if n == 1
    l = lucas(n - 1) + lucas(n - 2)
    @memo[n] = l
    return l
end

puts lucas(n)

