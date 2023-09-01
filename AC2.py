#1
def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_total = salario_por_hora * horas_trabalhadas
    return salario_total

salario_por_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_final = calcular_salario(salario_por_hora, horas_trabalhadas)
print("O salário a ser recebido é:", salario_final)

#2
def calcular_expressoes(num1, num2, num3):
    resultado1 = (2 * num1) * (0.5 * num2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    print("Resultado 1:", resultado1)
    print("Resultado 2:", resultado2)
    print("Resultado 3:", resultado3)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

calcular_expressoes(num1, num2, num3)

#3
def calcular_resultados(num1, num2, num3):
    resultado1 = (2 * num1) * (num2 / 2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3
    return resultado1, resultado2, resultado3

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado_total = calcular_resultados(numero1, numero2, numero3)
print("Resultados:", resultado_total)

#4
def is_leap_year(year):
    multiple_of_4 = (year % 4) == 0
    multiple_of_100 = (year % 100) == 0
    multiple_of_400 = (year % 400) == 0
    
    return multiple_of_4 and (not multiple_of_100 or multiple_of_400)

# Testes
print(is_leap_year(1995))  # False
print(is_leap_year(2012))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True


