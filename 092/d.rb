a, b = gets.strip.split.map(&:to_i)
HEIGHT = 100
WIDTH = 100

BLACK_PER_ROW = HEIGHT / 2


# 全部を白で塗っておく
table = []
HEIGHT.times do
  table << "." * WIDTH
end

# 黒の連結成分をを B - 1 個作る
# 1行に50個作れるので　必要な行数 = ((B - 1) + 49) / 50
black_lines = ((b - 1) + HEIGHT / 2 - 1) / (HEIGHT / 2)

# 黒に塗っていく
(b - 1).times do |i|
  row = (i / BLACK_PER_ROW) * 2
  col = (i - (i / BLACK_PER_ROW) * BLACK_PER_ROW) * 2
  # puts "i = #{i}, row = #{row}, col = #{col}"
  table[row][col] = '#'
end

# 残りで白の連結成分を作る
# 黒で塗られているところは高々10行目までしか来ないので
# 下から80行の間でなんとかする
limit = 20
white = a - 1
line = HEIGHT - 2
#黒の最後の連結成分を作成
(limit...HEIGHT).each do |i|
  table[i][0] = '#'
end

while line >= limit do
  if white <= 0
    break
  end
  # 黒で塗りつぶす
  table[line] = "#" * WIDTH
  line -= 2
  white -= 1
end

# まだ白の連結成分が足りない場合
# puts "white = #{white}"
if white > 0
  line = HEIGHT - 1
  col = 2
  while white > 0
    # puts "aaaaaaaaaaaa"
    table[line][col] = '#'
    col += 2
    white -= 1
    if col >= WIDTH
      col = 2
      line -= 2
    end
  end
end

def print_table(table)
  HEIGHT.times do |i|
    puts table[i]
  end
end

puts "#{HEIGHT} #{WIDTH}"
print_table(table)
