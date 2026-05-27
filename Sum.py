t = int(input())

for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    print("YES" if a + b == c else "NO")