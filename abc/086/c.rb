n = gets.to_i
data = []
data << [0, 0, 0]
n.times do
    t, x, y = gets.strip.split.map(&:to_i)
    data << [t, x, y]
end

def is_reachable t1, x1, y1, t2, x2, y2
    # 次の地点までのマンハッタン距離
    d = (x2 - x1).abs + (y2 - y1).abs
    # かけたい時間
    t = t2 - t1
    # 最短ルートで行っても間に合わない
    return false if t < d

    # 余裕がある時、行ったり来たりで調整できるか？
    return (d - t) % 2 == 0
end

reachable = true
for i in (0...n)
    t1, x1, y1 = data[i]
    t2, x2, y2 = data[i + 1]
    unless is_reachable(t1, x1, y1, t2, x2, y2)
        reachable = false
        break
    end
end

if reachable
    puts 'Yes'
else
    puts 'No'
end


