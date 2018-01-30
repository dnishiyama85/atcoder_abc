require 'pp'

@n = gets.to_i
@cs, @ss, @fs = [], [], []
(@n-1).times do |i|
    c, s, f = gets.strip.split.map(&:to_i)
    @cs << c
    @ss << s
    @fs << f
end

# 今の時刻と今いる駅から、次の駅の到着時刻を返す
def next_train now, where
    return @ss[where] + @cs[where] if now <= @ss[where]
    return now + @cs[where] if now % @fs[where] == 0
    now + (@fs[where] - now % @fs[where]) + @cs[where]
end

# i からスタートした人がゴールにつくのにかかる時間
def solve_for i
    (i..@n-2).inject(0) { |acc, j| next_train(acc, j) }
end

@n.times do |i|
    puts solve_for i
end
