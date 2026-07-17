produto = {
    "nome": "Arroz",
    "preco": 25.50,
    "quantidade": 10
}

print(type(produto))
print(produto["nome"])
print(produto["preco"])

produto["preco"] = 30.00

print(produto)

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, valor)

if "preco" in produto:
    print("A chave existe")

turma = {
    "professor": "João",
    "curso": "Análise e Desenvolvimento de Sistemas",
    "alunos": [
        {"nome": "Ana", "idade": 20},
        {"nome": "Gabriel", "idade": 22}
    ]
}

print(turma["alunos"][1]["nome"])