data = gets.strip.split.map(&:to_i).sort
@step = 0

def next_step(data)
  a, b, c = data
  # 10 10 10
  if a == b && b == c
    return data
  end
  # 9 10 10
  if b == c && b - a == 1
    data[0] += 2
    data[1] += 1
    data[2] += 1
    @step += 2
    return data
  end

  # 8 10 10
  if b == c && b - a == 2
    data[0] += 2
    @step += 1
    return data
  end

  # 9 9 10
  if a == b && c - b == 1
    data[0] += 1
    data[1] += 1
    @step += 1
    return data
  end

  # 8 8 10
  if a == b && c - b == 2
    data[0] += 2
    data[1] += 2
    @step += 2
    return data
  end

  # 7 9 10
  if c - b == 1 && b - a > 1
    data[0] += 1
    data[1] += 1
    @step += 1
    return data
  end

  # 5 8 10
  if b < c - 1 && a < b
    data[0] += 2
    @step += 1
    return data
  end

  if a < b && b < c
    data[0] += 1
    data[1] += 1
    @step += 1
    return data
  end

  # 1 8 10
  if b < c - 1
    data[1] += 2
    @step += 1
    return data
  end

  if a == b
    data[0] += 1
    data[1] += 1
    @step += 1
    return data
  end

  if b == c && b - a > 2
    data[0] += 2
    @step += 1
  end

  data[0] += 2
  @step += 1
  return data

end

while true
  a, b, c = data
  # p data
  # puts "step = #{@step}"
  if a == b && b == c
    break
  end
  data = next_step(data).sort
end

puts @step
