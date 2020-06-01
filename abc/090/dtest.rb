N = 170
b = 11
k = 3

puts "N = #{N}, b = #{b}, k = #{k}"
for q in k...b do
    m = (N - q) / b
    puts "q = #{q}, m = #{m}"
end

