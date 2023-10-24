#1
def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    n = int(input("Digite o valor de n: "))
    imprimir_padrao(n)

if __name__ == "__main__":
    main()

#2
def contar_digitos(numero):
    numero_str = str(numero)
    quantidade_digitos = len(numero_str)
    return quantidade_digitos

def main():
    numero = int(input("Digite um número inteiro: "))
    quantidade = contar_digitos(numero)
    print(f'O número {numero} tem {quantidade} dígitos.')

if __name__ == "__main__":
    main()

#3
try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    resultado = num1 / num2

except ValueError:
    print("Erro: Um ou ambos os valores inseridos não são inteiros.")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

finally:
    try:
        print("O resultado da divisão é:", resultado)
    except NameError:
        print("A divisão não foi executada devido a erros anteriores.")
