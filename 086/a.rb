a, b = gets.strip.split.map(&:to_i)
if a * b % 2 == 0
    puts 'Even'
else
    puts 'Odd'
end

