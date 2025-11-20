amount = int(input())
denom = int(input())

notes = {}

while amount > 0:
    match denom:
        case 100:
            notes[100] = amount // 100
            amount %= 100
            denom = 50
        case 50:
            notes[50] = amount // 50
            amount %= 50
            denom = 20
        case 20:
            notes[20] = amount // 20
            amount %= 20
            denom = 10
        case 10:
            notes[10] = amount // 10
            amount %= 10
            denom = 5
        case 5:
            notes[5] = amount // 5
            amount %= 5
            denom = 2
        case 2:
            notes[2] = amount // 2
            amount %= 2
            denom = 1
        case 1:
            notes[1] = amount // 1
            amount %= 1

for d in [50, 20, 10, 5, 2, 1]:
    print(f"{d} rupees note: {notes.get(d,0)}")