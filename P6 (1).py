n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])
    s = a + b
    print(int(str(s)[::-1]))