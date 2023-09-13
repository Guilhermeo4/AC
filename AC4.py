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

print(e_primo(13))  
print(e_primo(12))  

#2

juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

def calcula_juros(valor_da_divida, quantidade_de_parcelas):
  return valor_da_divida * juros[quantidade_de_parcelas] / 100

def calcula_valor_total_da_divida(valor_da_divida, quantidade_de_parcelas, juros):
  return valor_da_divida + juros


def calcula_valor_da_parcela(valor_total_da_divida, quantidade_de_parcelas):
  return valor_total_da_divida / quantidade_de_parcelas


valor_da_divida = float(input("Digite o valor da dívida: "))

for quantidade_de_parcelas in juros.keys():
  juros = calcula_juros(valor_da_divida, quantidade_de_parcelas)
  valor_total_da_divida = calcula_valor_total_da_divida(valor_da_divida, quantidade_de_parcelas, juros)
  valor_da_parcela = calcula_valor_da_parcela(valor_total_da_divida, quantidade_de_parcelas)
  print(
    f"Quantidade de parcelas: {quantidade_de_parcelas}\n"
    f"Juros: {juros}\n"
    f"Valor total da dívida: {valor_total_da_divida}\n"
    f"Valor da parcela: {valor_da_parcela}"
  )

  print(f"Valor da parcela: {valor_da_parcela:.2f}")

  #3

intervalos = {
    "0-25": 0,
    "26-50": 0,
    "51-75": 0,
    "76-100": 0
}

while True:
  numero = float(input("Digite um número: "))
  if numero < 0:
    break

  for intervalo in intervalos.keys():
    if numero >= intervalo[0] and numero <= intervalo[1]:
      intervalos[intervalo] += 1

for intervalo, quantidade in intervalos.items():
  print(f"{quantidade} números entre {intervalo[0]} e {intervalo[1]}")






