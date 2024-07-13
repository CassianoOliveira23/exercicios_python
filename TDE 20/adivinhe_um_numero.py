'''1- Adivinhe o número de 0 a 20 
Crie um programa em Python no qual o computador escolhe um número aleatório de 0 a 20, e o jogador deve tentar adivinhar qual é esse número. O programa deve fornecer dicas para ajudar o jogador a chegar ao número correto.

O programa deve seguir as seguintes especificações:

O computador escolhe um número aleatório de 0 a 20 usando o módulo random.

O programa solicita ao jogador que insira um palpite.

O programa verifica se o palpite do jogador é válido, ou seja, se está dentro do intervalo de 0 a 20.

Se o palpite for inválido, o programa exibe uma mensagem de erro e solicita ao jogador que insira um novo palpite.

Se o palpite for válido, o programa compara o palpite do jogador com o número escolhido pelo computador.

Se o palpite for igual ao número escolhido, o programa exibe uma mensagem de acerto e termina.

Se o palpite for diferente do número escolhido, o programa fornece dicas ao jogador (por exemplo, "O número é maior" ou "O número é menor") e retorna ao passo 2, solicitando um novo palpite ao jogador.

O programa permite um número limitado de tentativas (por exemplo, 3 tentativas) antes de encerrar o jogo.
Se o jogador não acertar o número dentro do número limite de tentativas, o programa exibe uma mensagem informando o número correto e encerra o jogo.
Ao final informe o tempo gasto no jogo.
Divirta-se tentando adivinhar o número escolhido pelo computador'''


import random as r
import datetime as dt

data_inicio = dt.datetime.now()

tentativas = 0
num_sorteado = r.randint(0, 20)

while tentativas < 3:
    num_escolhido = int(input("Escolha um número de 0 a 20: "))

    if num_escolhido < 0 or num_escolhido > 20:
        print("Número fora do intervalo permitido. Por favor, digite um número entre 0 e 20.")
        continue

    tentativas += 1

    if num_escolhido == num_sorteado:
        print("Parabéns, você ganhou!!!")
        break

    elif num_escolhido < num_sorteado:
        print("Tente um número maior.")

    else:
        print("Tente um número menor.")

print(f"O número correto é {num_sorteado}\nFim de jogo")

data_fim = dt.datetime.now()
tempo_gasto = (data_fim - data_inicio).total_seconds()
print(f"Você levou {tempo_gasto} segundos jogando.")










'''import random as r
import datetime as dt

data_inicio = dt.datetime.now()


tentativas = 0


num_sorteado = r.randint(0,20)

while tentativas < 3:
    num_escolhido = int(input("Escolha um número de 0 a 20: "))


    # verificar se o número está no intervalo
    if not num_escolhido or int(num_escolhido) < 0 or int(num_escolhido)  > 20:
        print("Numero fora do intervalo permitido. Por favor digite um número entre 0 e 20.")
        continue

    num_escolhido = int(num_escolhido)
    tentativas += 1

    if num_escolhido == num_sorteado:
        print("Parabéns você ganhou!!!")
        break
        

    elif num_escolhido < num_sorteado:
        print("Tente um número maior")
        tentativas += 1

    else:
        print("Tente um número menor.")  
        tentativas += 1      

print(f"O número correto é {num_sorteado}\nFim de jogo")

data_fim = dt.datetime.now()
tempo_gasto = data_fim - data_inicio
print(f"Voce levou {tempo_gasto} jogando")'''
