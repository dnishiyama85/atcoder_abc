a, b = gets.strip.split
c = (a + b).to_i

def is_square n
    up = Math.sqrt(n)
    for i in (1..up)
        if i * i == n
            return true
        end
    end
    false
end

if is_square c
    puts 'Yes'
else
    puts 'No'
end
