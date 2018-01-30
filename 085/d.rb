n, h = gets.strip.split.map(&:to_i)
as = []
bs = []

n.times do
    a, b = gets.strip.split.map(&:to_i)
    as << a
    bs << b
end

# 最強の振るいの攻撃力
max_furui = as.max

# 投げの合計攻撃力
total_throw = bs.sum


# 
