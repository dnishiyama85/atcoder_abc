n, m = gets.strip.split.map(&:to_i)
cakes = []

n.times do
    cakes << gets.strip.split.map(&:to_i)
end

patterns = [
    [+1, +1, +1],
    [+1, +1, -1],
    [+1, -1, +1],
    [+1, -1, -1],
    [-1, +1, +1],
    [-1, +1, -1],
    [-1, -1, +1],
    [-1, -1, -1],
]

mxs = []

patterns.each do |p|
    score = cakes.map.with_index { |cake, i| [i, cake[0] * p[0] + cake[1] * p[1] + cake[2] * p[2]] }
    ranking = score.sort_by { |s| s[1] }.reverse
    leaders = []
    m.times do |i|
        leaders << cakes[ranking[i][0]]
    end
    x = 0
    leaders.each do |cake|
        x += cake[0]
    end

    y = 0
    leaders.each do |cake|
        y += cake[1]
    end

    z = 0
    leaders.each do |cake|
        z += cake[2]
    end

    total = x.abs + y.abs + z.abs
    mxs << total
end

puts mxs.max

