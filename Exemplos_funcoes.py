import re

# def saudacao():
#     print("Boa noite!")
#
# saudacao()

def saudacao(nome):
    print(f"Boa noite {nome}!")

saudacao("Allan")
saudacao("William")

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcular_media(8, 10)
print(f"A média é {resultado}")


def calcular_imc(peso, altura):
     return peso / altura ** 2

imc = calcular_imc(70, 1.75)
print(f"Seu IMC é: {imc:.2f}")


def validar_email(email):
    regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    if re.match(regex, email):
        return True
    else:
        return False

print(validar_email("ana@email.com"))
