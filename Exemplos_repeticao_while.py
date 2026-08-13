contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# Contador de vogais em uma palavra
palavra = input("Digite uma palavra: ")
i = 0
vogais = 0

while i < len(palavra):
    if palavra[i].lower() in "aeiou":
        vogais += 1
    i += 1
print(f"Quantidade de vogais: {vogais}")


# Tabuada de um número esolhido pelo usuário
numero = int(input("Digite um número: "))

contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1


# Tabuada do 1 ao 10
numero = 1
while numero <= 10:
    print(f"\nTabuada do {numero}")

    contador = 1
    while contador <= 10:
        print(f"{numero} x {contador} = {numero * contador}")
        contador += 1

    numero += 1
