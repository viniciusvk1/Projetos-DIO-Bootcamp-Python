def is_vegan(option):
    return option.lower() == "s"


def main():
    num_pedidos = int(input())
    pedidos = []

    for i in range(1, num_pedidos + 1):
        nome_prato = input()
        calorias = int(input())
        vegano = input()

        pedidos.append((nome_prato, calorias, is_vegan(vegano)))

    print()
    for i, pedido in enumerate(pedidos, 1):
        nome_prato, calorias, vegano = pedido
        tipo_vegano = "Vegano" if vegano else "Nao-vegano"
        print(f"Pedido {i}: {nome_prato} ({tipo_vegano}) - {calorias} calorias")


if __name__ == "__main__":
    main()
