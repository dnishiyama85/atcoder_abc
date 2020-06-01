k = gets.to_i

cnt = 0
i = 1

while cnt < k

    if cnt % 10 == 0
        i = 1
    end

    if cnt < 10
        puts i
        i += 1
    elsif cnt < 20
        puts i * 10 + 9
        i += 1
    end

    cnt += 1

end
