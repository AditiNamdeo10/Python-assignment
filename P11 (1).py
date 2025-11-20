N = int(input())

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())
    start = SH * 60 + SM
    end = EH * 60 + EM
    duration = end - start
    hours = duration // 60
    minutes = duration % 60
    print(hours, minutes)