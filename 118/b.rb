n, m = gets.strip.split.map(&:to_i)
list = [0] * m

n.times do
    ans = gets.strip.split.map(&:to_i)
    ans.shift
    ans.each do |a|
        list[a - 1] += 1
    end
end

cnt = list.select { |item| item == n }.size

puts cnt

