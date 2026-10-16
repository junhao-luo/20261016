n = int(input("n: "))
for i in range(1, n + 1):
    for j in range (1, n + 1):
        print(f"{i * j:6d}", end="")
    print()