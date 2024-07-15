# 8. Faça um programa para cálculos de multas de um determinado número de veículos. O programa deve ler a velocidade de um veículo e perguntar ao usuário se ele deseja inserir a velocidade de mais algum veículo, use “sim” para continuar e “não” para sair do loop. 

# Considere que a velocidade máxima da rodovia é de 60km/h e a margem de erro do é 7km/h até 100 km/h, e 7% quando o veículo estiver acima de 100 km/h.

# São 3 valores para a multa por excesso de velocidade: 
# ●	Até 20% acima do limite permitido: R$130,16. Multa média.
# ●	De 20% até 50% acima do limite permitido: R$195,23. Multa grave.
# ●	Acima de 50% do limite permitido: R$880,41. Multa gravíssima.

#Ao término da leitura, informar:
# ●	Quantos veículos não tiveram multas.
# ●	Quantos veículos tiveram multa média.
# ●	Quantos veículos tiveram multa grave.
# ●	Quantos veículos tiveram multa gravíssima.
# ●	Imprimir o somatório total das multas.
# ●	Imprimir a média de velocidade da rodovia.




#resposta = "sim"

#while resposta == "sim":
    #velocidade = float(input("Digite a velocidade: "))
    #resposta = input("Você deseja inserir mais algum veículo?")

resp = '' 
tot_v = 0 
q_multas = 0  
s_multa = 0  
m_multa = 0 
g_multa = 0  
gs_multa = 0 
soma = 0 



while resp == "não":
    resp = str(input("Deseja continuar? sim ou não: "))
    if resp == "sim":
        v_car = int(input("Digite a velocidade do carro em Km/h: "))

        tot_v += v_car
        q_multas += 1
        if v_car > 60 and v_car <= 67:
            print(f"Velocidade do carro: {v_car} Km/h. Dentro da margem de erro. Multa não aplicada.")
            s_multa += 1
        elif v_car > 67 and v_car <= 60+(60*0.2):
            print(f"Velocidade do carro: {v_car} Km/h. Multa aplicada R$ 130,16. MULTA MÉDIA.")
            m_multa += 1
            soma += 130.16
        elif v_car > 60+(60 * 0.2) and v_car <= 60+(60 * 0.5):
            print(f"Velocidade do carro: {v_car} Km/h. Multa aplicada. R$195,23 - MULTA GRAVE.")
            g_multa += 1 
            soma += 195.23
        elif v_car > 60 + (60 * 0.5):
             print(f"Velocidade do carro: {v_car} Km/h. Multa aplicada. R$195,23 - Multa grave.")
             g_multa += 1
             soma += 195.23
        else:
            print(f"Velocidade do carro: {v_car} Km/h. Dentro da velocidade permitida. Dirija com segurança.")
            s_multa += 1
        continue
    elif resp == "não" or resp == "nao":
        break
    else:
        print("Resposta Inválida!")
        continue





print(f"Número de veículos contados: {q_multas}") 

print(f"Número de veículos sem multas: {s_multa}") 

print(f"Número de veículos com multa média: {m_multa}") 

print(f"Número de veículos com multa grave: {g_multa}") 

print(f"Número de veículos com multa gravíssima: {gs_multa}") 

print(f"A soma de todas as multas foi de R${soma}") 

print(f"A velocidade média na rodovia foi de {tot_v/q_multas}Km/h.") 


