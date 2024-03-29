""""
Imagine que você está criando um aplicativo de entrega de comida e precisa informar ao usuário
o tempo estimado de entrega de um restaurante. A mensagem deve conter
o nome do restaurante e o tempo estimado de entrega em minutos.

A entrada deverá receber os valores abaixo:

nomeRestaurante (string): o nome do restaurante desejado.
tempoEstimadoEntrega (number): o tempo estimado de entrega em minutos.

Deverá retornar uma mensagem (string) informando ao usuário o tempo estimado de entrega do restaurante.
Por exemplo, para o restaurante Bar do Zinho com o tempo estimado de entrega sendo 20, imprima:

O restaurante Bar do Zinho entrega em 20 minutos.
"""

nome_restaurante = input()
tempoEstimadoEntrega = int(input())

print("O restaurante {} entrega em {} minutos.".format(nome_restaurante, tempoEstimadoEntrega))