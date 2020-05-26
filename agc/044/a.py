from collections import deque

T = int(input())


for t in range(T):
    n, a, b, c, d = map(int, input().strip().split())
    queue = deque()
    queue.append(n)
    coins = {n: 0}
    import pdb; pdb.set_trace()
    while len(queue) > 0:
        current = queue.popleft()
        if current == 1:
            print(coins)
            break

        for m, coin in zip([5, 3, 2], [c, b, a]):
            rm = current % m
            qm = current // m
            if rm == 0 and (qm not in coins):
                coins[qm] = coins[current] + coin
                queue.append(qm)
            else:
                delta_m_plus = m - rm
                cm_plus = current + delta_m_plus
                if cm_plus not in coins:
                    coins[cm_plus] = coins[current] + d * delta_m_plus
                    queue.append(cm_plus)

                delta_m_minus = rm
                cm_minus = current - delta_m_minus
                if cm_minus not in coins:
                    coins[cm_minus] = coins[current] + d * delta_m_minus

    print(coins[current] + d)

