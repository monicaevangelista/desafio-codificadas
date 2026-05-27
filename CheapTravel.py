n, m, a, b = map(int, input().split())

custo1 = n * a

pacotes = n // m
resto = n % m
custo2 = pacotes * b + resto * a

custo3 = ((n + m - 1) // m) * b

print(min(custo1, custo2, custo3))