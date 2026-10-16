n, m = map(int, input("n m: ").split())

x = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(m):
            print(f"{x:4d}", end="")
            x += 1
        print()
    else:
        for j in range(x + m - 1, x - 1, -1):
            print(f"{j:4d}", end="")
        x += m
        print()