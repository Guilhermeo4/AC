#1
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

faixas_reajuste = [(0, 400.00, 15), (400.01, 800.00, 12), (800.01, 1200.00, 10), (1200.01, 2000.00, 7)]

percentual_aumento = 0

for faixa in faixas_reajuste:
    if salario_atual >= faixa[0] and salario_atual <= faixa[1]:
        percentual_aumento = faixa[2]
        break

aumento = (salario_atual * percentual_aumento) / 100

novo_salario = salario_atual + aumento

print("\nResumo do Reajuste Salarial:")
print("Salário antes do reajuste: R$ {:.2f}".format(salario_atual))
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))

#2
def dia_da_semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5:
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sábado"
    else:
        return "Valor inválido"

try:
    numero = int(input("Digite um número de 1 a 7: "))
    resultado = dia_da_semana(numero)
    print("Dia correspondente da semana:", resultado)
except ValueError:
    print("Por favor, insira um número válido.")

#3
import math

a = float(input("Digite o valor de a: "))
if a == 0:
    print("O valor de 'a' não pode ser igual a zero. A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais, pois o delta é negativo.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1}")
        print(f"Raiz 2: {raiz2}")

