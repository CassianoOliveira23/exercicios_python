'''2- Jogo de Dados - Duelo de Jogadores
● Crie um programa em Python que simule um jogo de dados entre dois
jogadores. Cada jogador lança um dado em cada rodada, e o objetivo é
acumular pontos para determinar o vencedor.
● O programa deve seguir as seguintes especificações:
● Cada jogador joga um dado (gera um número aleatório de 1 a 6) em cada
rodada.
● A cada rodada, o programa exibe o resultado do lançamento de cada jogador.
○ Informe o vencedor da rodada ou se houve empate.
● Os resultados dos lançamentos de dados são armazenados em listas
separadas para cada jogador.
● O programa repete o processo de lançamento de dados por 10 rodadas.
● Ao final das 10 rodadas, o programa exibe a pontuação total de cada jogador.
○ Utilize as listas para somar os valores dos lançamentos em cada
rodada.
● Armazena os resultados de cada rodada em um arquivo de texto.
● O programa determina o vencedor com base nas pontuações totais:
● Se um jogador tiver uma pontuação maior que o outro, ele é declarado o
vencedor.
● Se ambos os jogadores tiverem a mesma pontuação, o programa declara um
empate.
○ Critério de desempate número de vitórias.
Você pode implementar esse jogo utilizando estruturas de repetição (como loops for
ou while), listas para armazenar os resultados dos lançamentos de dados, funções
do módulo random para gerar os números..
Divirta-se jogando e descubra quem será o campeão do jogo de dados!'''


import random as r
from time import sleep
import io

with io.open('resultado.txt', 'a') as file:
    file.write('\nJOGO DE DADOS')
    

pts_jogador1 = []
pts_jogador2 = []

vit_j1 = 0
vit_j2 = 0

j1_nome = str(input("Nome do  jogador 1: "))
j2_nome = str(input("Nome do  jogador 2: "))
print()

for i in range(10):

    j1 = r.randint(1, 6)
    pts_jogador1.append(j1)
    print(f"Jogador {j1_nome} tirou {j1}")
    with io.open('resultado.txt', 'a') as file:
        file.write((f"\nJogador {j1_nome} tirou {j1}"))
        sleep(1)

    j2 = r.randint(1, 6)
    pts_jogador2.append(j2)
    print(f"Jogador {j2_nome} tirou {j2}")
    with io.open('resultado.txt', 'a') as file:
        file.write((f"\nJogador {j2_nome} tirou {j2}"))
        
        sleep(1)
    

    if (j1 == j2):
        print('Houve empate')
        with io.open('resultado.txt', 'a') as file:
            file.write('\nEMPATE')
        print()
        
    elif (j1 > j2):
        print(f"O jogador {j1_nome} venceu!")
        with io.open('resultado.txt', 'a') as file:
            file.write((f"O jogador {j1_nome} venceu!"))
        print()
        vit_j1 += 1

    else:
        print(f"O jogador {j2_nome} venceu!")
        with io.open('resultado.txt', 'a') as file:
            file.write((f"O jogador {j2_nome} venceu!"))
        print() 
        vit_j2 += 1



# fazer a soma total, comparar: 

sum(pts_jogador1) 
print(f"Pontuação total do jogador {j1_nome}: {sum(pts_jogador1)} ")

sum(pts_jogador2) 
print(f"Pontuação total do jogador {j2_nome}: {sum(pts_jogador2)} ")



if pts_jogador1 > pts_jogador2:
    print(f"O campeão é: {j1_nome}. Com {vit_j1} vitórias")


elif pts_jogador2 > pts_jogador1:
    print(f"O campeão é: {j2_nome}. Com {vit_j2} vitórias")

else:
    if vit_j1 > vit_j2:
        print(f"No critério de desempate, o  jogador {j1_nome} é o campeão pelo número de vitótias({vit_j1})")
    elif vit_j2 > vit_j1:
        print(f"No critério de desempate, o  jogador {j2_nome} é o campeão pelo número de vitótias({vit_j1})")
    else:   
        print("Houve empate")   
   
      





    