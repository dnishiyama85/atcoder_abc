n, m = gets.strip.split.map(&:to_i)
as = gets.strip.split.map(&:to_i)

@dict = {
    1 => 2,
    2 => 5,
    3 => 5,
    4 => 4,
    5 => 5,
    6 => 6,
    7 => 3,
    8 => 7,
    9 => 6,
}

@inv = {
    2 => 1,
    3 => 7,
    4 => 4,
    5 => 5,
    6 => 9,
    7 => 8,
}

availables = as.map { |a| @dict[a] }.sort

# 一番コスパのいい数字を並べまくる
min_cost = availables[0]

# 何桁並べられるか
num_digit = n / min_cost

# あと何本余っているか
residue = n % min_cost

# 本数を増やすことで大きい数字に変えられるか
def larger(num, as)
   # num を作るのに必要な本数
   match = @dict[num]
   # それより多い本数が必要な数字
   cand = @dict.select { |k,v| v > match && k > num && as.include?(k) }.keys
   return cand
end

# 本数を増やすことで小さい数字に変えられるか
def smaller(num, as)
    match = @dict[num]
    cand = @dict.select { |k,v| v > match && k < num && as.include?(k) }.keys
    return cand
end

d = @inv[min_cost]
digits = [d] * num_digit
while residue > 0 do
    # 最上位の数を大きい数字に変えられるか
    largers = larger(d, as)
    break if largers.empty?
    largers = largers.select { |l| @dict[l] <= residue }
    break if largers.empty?
    largest = largers.max
    digits.unshift(largest)
    digits.pop
    residue -= @dict[largest]
end

# 最下位の数を小さい数字に変えられるか
smallers = smaller(d, as)
largest = @dict.select { |k, v| v - @dict[d] == residue && smallers.include?(k)}.keys.max
digits.pop
digits.push(largest)

puts digits.join


