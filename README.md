# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|

| 1 | 1742A A. Sum          | [Ver no Codeforces](https://codeforces.com/problemset/problem/1742/A) |  800 |
| 2 | 805B	B. 3-palindrome  | [Ver no Codeforces](https://codeforces.com/problemset/problem/805/B)  | 1000 |
| 3 | 466A A. Cheap Travel  | [Ver no Codeforces](https://codeforces.com/problemset/problem/466/A)  | 1200 |
 
 
---
 
## Problema 1 — A. Sum
 
### O que o problema pede?
O problema solicita primeiro que seja informado um número de testes. Para cada teste, devem ser recebidos três números inteiros. Em seguida, é necessário verificar se um desses números é igual à soma dos outros dois. Se essa condição for verdadeira, deve ser impresso “SIM”; caso contrário, “NÃO”.
 
 
### Como eu resolvi?
Optei por usar Python por ser uma linguagem mais simples e com menor quantidade de código para resolver o problema.

Primeiro, busquei entender bem a lógica do exercício e utilizei o ChatGPT como apoio durante o processo, além de seguir orientações do vídeo do professor Fábio.

A principal dificuldade foi executar o código corretamente no VSCode, já que tive alguns problemas com o ambiente. Após tirar dúvidas com a IA, consegui ajustar a execução e rodar o programa sem erros.

No final, compreendi a lógica do problema e utilizei a estrutura de repetição for para resolver cada caso de teste de forma correta e organizada.
 
 
### Código
```python
t = int(input())

for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    print("YES" if a + b == c else "NO")
```
 
---
 
## Problema 2 — 805B	B. 3-palindrome
 
### O que o problema pede?
O problema pede para criar uma string com `n` letras usando apenas `a`, `b` e `c`, sem repetir a mesma letra com distância de 2 posições.

 
### Como eu resolvi?
 Primeiro procurei entender a lógica do problema e percebi que precisava evitar repetir a mesma letra com distância de 2 posições. Depois disso, criei uma lista vazia e percorri cada posição da string. Em cada passo, testei as letras a, b e c, escolhendo a primeira que não fosse igual à letra de duas posições antes. No final, juntei todas as letras para formar a string.
 
### Código
```python
n = int(input())
s = []

for i in range(n):
    for letra in "abc":
        if i < 2 or s[i-2] != letra:
            s.append(letra)
            break
print("".join(s))
```
 
---
 
## Problema 3 — A. Cheap Travel
 
### O que o problema pede?

O problema pede para descobrir a forma mais barata de fazer `n` viagens de metrô. Para isso, você pode pagar viagem por viagem ou usar um ticket que cobre várias viagens de uma vez. A ideia é escolher a opção que gasta menos dinheiro no final.

 
### Como eu resolvi?

Primeiro, entendi que precisava comparar formas diferentes de pagar as viagens. Depois, calculei o custo usando três estratégias: pagar todas as viagens individualmente, usar tickets de `m` viagens o máximo possível e completar o resto com tickets individuais, e também usar apenas tickets de `m` viagens. No final, escolhi o menor valor entre essas opções para encontrar a forma mais barata.

 
### Código
```python
n, m, a, b = map(int, input().split())

custo1 = n * a

pacotes = n // m
resto = n % m
custo2 = pacotes * b + resto * a

custo3 = ((n + m - 1) // m) * b

print(min(custo1, custo2, custo3))
```
 
<!-- Remova as linhas dos problemas que não foram resolvidos caso tenha escolhido menos de 3.-->

---
 
## IA utilizada
 
**Qual IA você usou?**
ChatGPT
 
**Como a IA te ajudou?**
A IA me ajudou a entender o problema, explicou a estratégia correta para resolvê-lo e identificou o erro na minha lógica inicial. Além disso, corrigiu o código, mostrou como executá-lo corretamente no ambiente Python e apresentou versões mais eficientes da solução, contribuindo também para meu aprendizado e evolução na forma de pensar problemas de programação.

---
 
## Reflexão
 
### Dificuldades encontradas
O mais difícil pra mim foi organizar tudo sem me perder no caminho.

Entender o problema foi o primeiro desafio, porque precisei transformar o enunciado em lógica. Depois que isso ficou claro, escrever o código ficou bem mais tranquilo. O GitHub acabou sendo mais uma questão de configuração e comandos, algo mais técnico.

No fim, o maior desafio não foi uma parte específica, mas conseguir juntar entendimento, lógica e ferramentas sem me confundir no processo.
 
 
### O que aprendi
Aprendi a transformar melhor o problema em lógica antes de sair escrevendo código. Percebi que quando eu entendo direito o enunciado, o código flui muito mais fácil e evito erro bobo.

Também aprendi a usar melhor o ambiente de execução, principalmente a diferença entre rodar Python e comandos do terminal, o que antes me confundia bastante.

E sobre IA, ficou claro pra mim que ela ajuda muito mais quando eu já tento pensar primeiro — ela não só “resolve”, mas também explica, corrige e me faz enxergar outras formas mais eficientes de fazer a mesma coisa.

 
 
### Como foi a experiência?
No geral, foi uma experiência bem interessante porque me fez pensar mais em lógica e não só em “fazer o código funcionar”.

O que eu mais gostei foi quando a solução começou a fazer sentido de verdade, depois que entendi o problema. A partir daí, ficou mais fácil ajustar o código e ver que existem formas mais simples de resolver a mesma coisa.

O que eu mudaria é ter perdido menos tempo com erros básicos de ambiente e já começar com uma estrutura mais organizada desde o início. Isso teria deixado o processo mais fluido e menos confuso.

