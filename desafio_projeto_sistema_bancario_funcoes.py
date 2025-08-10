def deposito(saldo, extrato, /):
    deposito = float(input("Valor do depósito: "))
    
    if deposito >= 0:
        saldo += deposito
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        return saldo, extrato
    
    else:
        print("Valor inválido. Recomece a operação.")

def saque(*, saldo, extrato, numero_saques):

    
    saque = float(input("Valor do saque: "))

    if saque > saldo:
        print("Saldo insuficiente. Recomece a operação.")

    elif saque > LIMITE:
        print("Limite por operação excedido. O limite por operação é de R$ 500,00.")
        return saldo, extrato, numero_saques

    elif saque < 0:
        print("Valor inválido. Recomece a operação.")

    else:
        saldo -= saque
        numero_saques += 1
        print("Saque realizado com sucesso!")
        extrato += f"Saque: R$ {saque:.2f}\n"
        return saldo, extrato, numero_saques

def mostrar_extrato(saldo,/, *, extrato):
    print(f" EXTRATO ".center(27, "*"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def new_user(usuarios):
    cpf = input("Informe o CPF do Usuário (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Erro! Usuário já cadastrado.")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Data de Nascimento (DD/MM/YYYY): ")
        endereco = input("Endereço: Logradouro, Nº, Bairro, Cidade, Estado (Sigla), Código Postal: ")
        usuarios.append({"nome": nome, "Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})
        print("Usuário cadastrado com sucesso!")

def new_account(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado. Recomece a operação.")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        print(f"""
\tAgência: \t{conta['agencia']}
\tC/C: \t{conta['numero_conta']}
\tTitular: \t{conta['usuario']['nome']}
              """)


def sair():
    print("Obrigado por usar nossos serviços!")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Contas
[7] Sair

=> """

opcoes = ["1", "2", "3", "4", "5", "6", "7"]
saldo = 1000
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = 1
numero_conta = 1

while True: 
    opcao = (input(menu))

    if opcao not in opcoes:
        print("Valor digitado é inválido. Escolha uma das opções.")
        continue

    match opcao:
        case "1":
            saldo, extrato = deposito(saldo, extrato)
    
        case "2":
            if numero_saques == LIMITE_SAQUES:
                print("Limite de saques diários excedido. Tente novamente amanhã.")
                continue
            else:
                saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques)


        case "3":
            mostrar_extrato(saldo, extrato=extrato)
        
        case "4":
            new_user(usuarios)

        case "5":
            conta = new_account(AGENCIA,numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        case "6":
            listar_contas(contas)

        case "7":
            sair()
            break