n = int(input())
s = []

for i in range(n):
    for letra in "abc":
        if i < 2 or s[i-2] != letra:
            s.append(letra)
            break
print("".join(s))