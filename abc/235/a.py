a, b, c = list(map(int, list(input().strip())))

abc = 100 * a + 10 * b + c
bca = 100 * b + 10 * c + a
cab = 100 * c + 10 * a + b

ans = abc + bca + cab

print(ans)
