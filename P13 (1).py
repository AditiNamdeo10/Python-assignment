N = int(input())
i = 1
while True:
    if N <= i:
        print("Ramesh")
        break
    N -= i
    if N <= i * 2:
        print("Suresh")
        break
    N -= i * 2
    i += 1