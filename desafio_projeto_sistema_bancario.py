menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Valor do depósito: "))

        if deposito >= 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")

        else:
            print("Valor inválido. Recomece a operação.")
    
    elif opcao == 2:

        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques diários excedido. Tente novamente amanhã.")
            continue
            
        saque = float(input("Valor do saque: "))

        if saque > saldo:
            print("Saldo insuficiente. Recomece a operação.")
        
        elif saque > LIMITE:
            print("Limite por operação excedido. O limite por operação é de R$ 500,00.")
        
        elif saque < 0:
            print("Valor inválido. Recomece a operação.")
        
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == 3:
        print(f" EXTRATO ".center(27, "*"))
        print("Não foram realizadas movimentações." if not extrato else extrato) # ADICIONADO APÓS A RESOLUÇÃO
        print(f"\nSaldo: R$ {saldo:.2f}")

    
    elif opcao == 4:
        print("Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação inválida. Selecione novamente a operação desejada.")
