
menu = """
[1] Depositar dinheiro em conta bancaria
[2]  Sacar dinheiro de conta bancaria
[3]  Gerar extrato de conta bancaria
[0] Sair do atendimento
"""

saldo_bancario = 0
limite_saque = 500
extrato_bancario = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    escolha = input(menu)

    if escolha == "1":
        valor_deposito = float(input("Informe o valor do deposito: "))

        if valor_deposito > 0:
            saldo_bancario += valor_deposito
            extrato_bancario += f"Deposito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operacao falhou! O valor informado e invalido.")

    elif escolha == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo_bancario
        excedeu_limite = valor_saque > limite_saque
        excedeu_saques = quantidade_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operacao falhou! Voce nao tem saldo suficiente.")
        elif excedeu_limite:
            print("A operacao falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("A operacao falhou! Numero maximo de saques excedido.")
        elif valor_saque > 0:
            saldo_bancario -= valor_saque
            extrato_bancario += f"Saque: R$ {valor_saque:.2f}\n"
            quantidade_saques += 1

        else:
            print("A operacao falhou! O valor informado e invalido.")

    elif escolha == "3":
        print("\n======================== EXTRATO ========================")
        print("Nao foram realizadas movimentacoes nessa conta bancaria." if not extrato_bancario else extrato_bancario)
        print(f"\nSaldo: R$ {saldo_bancario:.2f}")
        print("===========================================================")

    elif escolha == "0":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")

