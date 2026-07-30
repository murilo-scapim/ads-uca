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
