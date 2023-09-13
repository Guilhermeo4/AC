#1
def e_primo(num):
  
  if num < 2:
    return False

  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False

  return True
  if not e_primo(num):
    print("Os divisores de", num, "são:")
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      print(i)

print(e_primo(17))  
print(e_primo(18))  


#2
def calcular_juros(valor_divida, parcelas):
    if parcelas == 1:
        return 0
    elif parcelas == 3:
        return valor_divida * 0.10
    elif parcelas == 6:
        return valor_divida * 0.15
    elif parcelas == 9:
        return valor_divida * 0.20
    elif parcelas == 12:
        return valor_divida * 0.25
    else:
        return None

def calcular_total_divida(valor_divida, parcelas):
    juros = calcular_juros(valor_divida, parcelas)
    if juros is not None:
        return valor_divida + juros
    else:
        return None

def imprimir_opcoes(valor_divida):
    print("Quantidade de Parcelas  % de Juros Valor Total     Valor da Parcela")
    for parcelas in [1, 3, 6, 9, 12]:
        juros = calcular_juros(valor_divida, parcelas)
        total_divida = calcular_total_divida(valor_divida, parcelas)
        if juros is not None and total_divida is not None:
            valor_parcela = total_divida / parcelas
            print(f"{parcelas:<22} {juros:<13} R$ {total_divida:<13} {parcelas:<18} R$ {valor_parcela:.2f}")

valor_divida = float(input("Digite o valor da dívida: R$ "))
imprimir_opcoes(valor_divida)

#3
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break
    
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

print("Quantidade de números no intervalo [0-25]:"), int

