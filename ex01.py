a,b,c = map(int, input().split())
if 0 < a < c < b:
    for i in range(a, b + 1):
        if i % c == 0:
            print(i, end=', ')