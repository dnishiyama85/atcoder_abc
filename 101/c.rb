n, k = gets.strip.split.map(&:to_i)
as = gets.strip.split.map(&:to_i)

# まず1の場所を探す
i1 = as.index(1)

# 左端
il = [i1 - k + 1, 0].max

# 右端
ir = [i1 + k - 1, n - 1].min

def ceil(p, q)
    p % q == 0 ? p / q : p / q + 1
end

min = 10000000000
(il..i1).each do |left|
    # puts "left = #{left}, min = #{min}"
    if left == 0
        r = ceil(n - k, k - 1) + 1
        min = [r, min].min
        # puts "left = #{left}, new_min = #{min}"
    elsif left + k >= n - 1
        l = ceil(left, k - 1) + 1
        min = [l, min].min
    else
        both = ceil(n - ir, k - 1) + ceil(left, k - 1) + 1
        min = [both, min].min
        # puts "left = #{left}, new_min = #{min}"
    end
end

puts min

