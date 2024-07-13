'''2- Conversor de Moedas em Tempo Real
Crie um programa que solicite ao usuário um valor em reais (R$) e ofereça um
menu de opções para converter esse valor em dólar (USD), euro (EUR) ou peso
argentino (ARS). Além disso, você precisa obter as taxas de câmbio em tempo real
usando o módulo requests.
Requisitos do programa:
● O programa deve utilizar o módulo requests para fazer requisições à API de
cotações de moedas em tempo real.
● O programa deve exibir um menu de opções com as seguintes opções:
○ Converter para dólar (USD)
○ Converter para euro (EUR)
○ Converter para peso argentino (ARS)
○ Sair do programa
● O programa deve solicitar ao usuário que digite o valor em reais (R$) que
deseja converter.
● O programa deve obter as taxas de câmbio em tempo real usando a API de
cotações de moedas. Por exemplo, você pode usar a API do
ExchangeRate-API ou outra API semelhante para obter as taxas de câmbio
atualizadas.
● O programa deve realizar a conversão do valor informado para a moeda
escolhida pelo usuário com base nas taxas de câmbio obtidas.
● O programa deve exibir o valor convertido na moeda escolhida pelo usuário.
● O programa deve permitir que o usuário volte ao menu principal após realizar
uma conversão, para que ele possa escolher outra opção ou sair do
programa.'''


import requests
from time import sleep



def convert_dolar(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    
    if response.status_code == 200:
        data = response.json()
        taxa = data['rates']['USD']
        dolar = valor * taxa
    print(f"Valor em Reais R$ {valor:.2f}")
    print()

    return dolar

def convert_euro(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    
    if response.status_code == 200:
        data = response.json()
        taxa = data['rates']['EUR']
        euro = valor * taxa
    print(f"Valor em Reais R$ {valor:.2f}")
    print()
    
    return euro

def convert_peso(valor):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    
    if response.status_code == 200:
        data = response.json()
        taxa = data['rates']['ARS']
        peso = valor * taxa
    print(f"Valor em Reais R$ {valor:.2f}")
    print()
    
    return peso


print('''
        CONVERSOR DE MOEDAS

[1] Converter para Dólar (USD)
[2] Converter para EURO (EUR)
[3] Converter para Peso Argentino (ARS)
[0] Sair ''')
print()



while True:
    print('-'*50)
    valor = float(input("Digite o valor me Reais: "))
    opcao = int(input("Digite o número da opção desejada: "))
    print()

    if opcao == 1:
        valor_convertido = convert_dolar(valor)
        print(f'Valor convertido em Dólar US$ {valor_convertido} ')
        print()

    elif opcao == 2:
        valor_convertido = convert_euro(valor)
        print(f'Valor convertido para EURO € {valor_convertido} ')
        print()

    elif  opcao == 3:
        valor_convertido = convert_peso(valor)
        print(f'Valor convertido para Peso Argentino AR$ {valor_convertido} ')
        print()
          
    elif opcao == 0:
        print('Finalizando...')
        sleep(1)
        break
    else:
        print('Opção inválida!')  
              
print()
print('Programa finalizado.')
print()


