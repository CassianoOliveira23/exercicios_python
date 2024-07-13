'''1- Programa para Obter Informações do Computador
Criem um programa em Python que obtenha informações do computador do
usuário, como detalhes do sistema operacional, informações sobre o processador,
memória e armazenamento. Além disso, o programa deve ter um menu de opções
que permita ao usuário escolher qual informação ele deseja visualizar.
● O programa deve utilizar os seguintes módulos:
○ psutil: para obter informações do sistema e do hardware.
○ platform: para obter informações do sistema operacional.
○ cpuinfo: para obter informações detalhadas do processador (esse
módulo precisa ser instalado com o comando -> pip install py-cpuinfo
● O programa deve exibir um menu de opções para o usuário, permitindo que
ele escolha qual informação deseja visualizar. As opções podem incluir:
○ Informações do sistema operacional.
○ Informações do processador.
○ Informações de memória.
○ Informações de armazenamento (tamanho do HD e SSD).
● O programa deve implementar cada opção do menu usando as funções e
métodos apropriados dos módulos psutil, platform e cpuinfo.
● O programa deve exibir as informações solicitadas de forma clara e
organizada.
○ Converta as informações de memória e armazenamento para GB.
● O programa deve permitir que o usuário volte ao menu principal após
visualizar uma informação, para que ele possa escolher outra opção ou sair
do programa.'''

import psutil
import platform
import cpuinfo
from time import sleep


def info_sistema_operacional():
    sistema = platform.system()
    versao = platform.release()
    print(f'Meu Sistema Operacional: {sistema} {versao}')
    print()


def info_processador():
    info = cpuinfo.get_cpu_info()
    model_name = info['brand_raw']
    architecture = info['arch']
    print(f'Processador:{model_name}\nArquitetura: {architecture}')
    print()


def info_memoria():
    memory = psutil.virtual_memory()
    total = round(memory.total / (1024**3), 2)
    avaiable= round(memory.available / (1024**3), 2)
    print(f'Memória Total do PC: {total} GB') 
    print(f'Memória disponível: {avaiable} GB')
    print()

def info_armazenamento():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'cdrom' not in partition.opts:
            usage = psutil.disk_usage(partition.mountpoint)
            total = round(usage.total/(1024**3), 2)
            print(f'Armazenamento\nDisco {partition.device}: {total} GB')
    print()


print('''
    INFORMAÇÕES DO COMPUTADOR

[1] Informações do Sistema Operacional
[2] Informações do Processador
[3] Informações da Memória RAM
[4] Informações do Armazenamento
[5] Sair              
''')

opcao = 0
while opcao != 5:
    opcao = int(input('Digite o número da opção desejada: '))

    if opcao == 1:
        info_sistema_operacional()
        print()
    elif opcao == 2:
        info_processador()
        print()
    elif opcao == 3:
        info_memoria()
        print()
    elif opcao == 4:   
        info_armazenamento()
        print()
    elif opcao == 5:
        print('Finalizado... ')
        sleep(1)
        break 
    else:
        print('Opção inválida!')   
        

    
print()
print('Programa Finalizado ')
print()