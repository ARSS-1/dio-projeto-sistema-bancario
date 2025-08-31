from abc import ABC,abstractmethod
from datetime import date, datetime

class Historico():
    def __init__(self):
        self.__transacoes = []

    @property
    def extrato(self):
        return self.__transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self.__transacoes.append(
            {
            "Tipo": transacao.__class__.__name__,
            "Valor": transacao.valor,
            "Data": datetime.now().strftime("%d-%m-%y %H:%M:%S")
            }
        )

class Conta():

    def __init__(self, cliente: Cliente, numero:int):
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = 0.0
        self.__agencia = "0001"
        self.__historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente: Cliente, numero:int) -> Conta:
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def extrato(self):
        return self.__historico.extrato
    
    def adicionar_transacao(self, transacao: Transacao):
        self.__historico.adicionar_transacao(transacao)
    
    def sacar(self, valor:float):

        if valor > self.__saldo:
            print("Saldo insuficiente. Recomece a operação.")
            return False
        elif valor <= 0:
            print("Valor inválido. Recomece a Operação.")
            return False
        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True

    def depositar(self, valor:float):

        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Erro ao realizar o depósito. Recomece a operação.")
            return False

class ContaCorrente(Conta):
    LIMITE_SAQUES = 3

    def __init__(self, cliente: Cliente, numero: int, limite: float):
        super().__init__(cliente, numero)
        self.limite = limite

class Cliente():
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.__contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta: Conta):
        self.__contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta: Conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    
    def registrar(self, conta: Conta):
        registro = conta.sacar(self.__valor)

        if registro:
            conta.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta: Conta):
        registro = conta.depositar(self.__valor)

        if registro:
            conta.adicionar_transacao(self)

    print("Obrigado por usar nossos serviços!")
