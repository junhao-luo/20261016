n,m = map(int, input("n m: ").split())
for i in range(1, n + 1):
    for j in range (1, m + 1):
        print(f"{i * j:6d}", end="")
    print()