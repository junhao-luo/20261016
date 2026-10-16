n, m = map(int, input("n m: ").split())

if n > 0 and m > 0:
    for i in range(1, n + 1):
        if i % 2 != 0:
            for j in range((i - 1) * m + 1, i * m + 1):
                print(f"{j:4d}", end="")
            print()
            
        else:  # Even rows: Right to Left
            for j in range(i * m, (i - 1) * m, -1):
                print(f"{j:4d}", end="")
            print()