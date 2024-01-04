'''

Autor : João Pedro Mendes

Desafio 1 - Projeto de sistema bancário

'''

menu = f"""
    =====MENU=====
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==============
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  #essa é uma constante por isso está em maiúsculo
valor_deposito = 0
valor_saque = 0
quantidade_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        print("Qual o valor que deseja depositar: ")
        valor_deposito = int(input())
        
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Seu saldo atual é RS {saldo:.2f}")
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            #print(extrato)
        else:
            print("Operação falou! O valor informado é inválido")

    elif opcao == "s":
        print("Saque")
        print("Qual o valor que deseja sacar: ")
        valor_saque = int(input())

        if quantidade_saques + 1 > LIMITE_SAQUES :
            print("A quantidade máxima de saques diários foi atingida volte amanhã")
        
        else:
            if valor_saque > 500:
                print("O valor máximo de saque permitido é R$ 500.00, estaremos retornando para o menu inicial")
            
            elif valor_saque > saldo:
                print("Não será possível sacar o dinheiro por falta de saldo, estaremos retornando para o menu inical")
                
            else:
                quantidade_saques += 1
                saldo -= valor_saque
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
                #print(extrato)
                print(f"Seu saldo atual é RS {saldo:.2f}")

    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"""
-------------------
Saldo Atual: R$ {saldo}       
              """)

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, por valor selecione novamente a operação desejada")
