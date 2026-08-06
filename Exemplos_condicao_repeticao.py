# Estruturas de repetição

for numero in range(10):
    print(numero)

print()
for i in range(1, 11):
    print(i)

# Lista é uma estrutura indexada
frutas = ["Maça", "Banana", "Laranja", "Morango"]

for i in range(len(frutas)):
    print(frutas[i])

print()
pessoas = [
    {"nome": "Ana", "peso": 60, "altura": 1.65},
    {"nome": "Gabriel", "peso": 85, "altura": 1.78},
    {"nome": "Ryan", "peso": 72, "altura": 1.70}
]
# Dicionário é uma estrutura chave/valor

for pessoa in pessoas:
    imc = pessoa["peso"] / (pessoa["altura"] ** 2)

    print(f"Nome: {pessoa["nome"]} IMC: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")


clientes = [
    {
        "nome": "Adecidio",
        "compras": [
            { "produto": "Arroz", "preco": 25.90, "quantidade": 2 },
            { "produto": "Feijão", "preco": 8.50, "quantidade": 3},
            { "produto": "Óleo", "preco": 7.20, "quantidade": 1},
        ]
    },
    {
        "nome": "Aline",
        "compras": [
            { "produto": "Café", "preco": 5.90, "quantidade": 6 },
            { "produto": "Leite", "preco": 18.90, "quantidade": 2},
        ]
    }
]

for cliente in clientes:
    total = 0

    print(f"\nCliente: {cliente["nome"]}")

    for produto in cliente["compras"]:
        subtotal = produto["preco"] * produto["quantidade"]
        total += subtotal

        print(f"Produto: {produto["produto"]}")
        print(f"Preço: R${produto["preco"]:.2f}")
        print(f"Quantidade: {produto["quantidade"]}")
        print(f"Subtotal: R${subtotal:.2f}")
    print(f"Total da compra: R${total:.2f}")
