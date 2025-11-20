N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    last_digit = a % 10
    cycle = [last_digit]
    for i in range(1, 4):
        cycle.append((cycle[-1] * last_digit) % 10)
    idx = (b - 1) % 4
    print(cycle[idx])