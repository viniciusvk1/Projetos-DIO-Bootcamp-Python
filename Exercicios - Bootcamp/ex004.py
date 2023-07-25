n = int(input())
pedidos = []
for i in range(n):
  nome, valor = input().split()
  valor = float(valor)
  pedidos.append((nome, valor))

desconto = input()

valor_total = 0
for nome, valor in pedidos:
  if desconto == "10%":
    valor_total += valor * 0.9
  elif desconto == "20%":
    valor_total += valor * 0.8

print("Valor total: {:.2f}".format(valor_total))