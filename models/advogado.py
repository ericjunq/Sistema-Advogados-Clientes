class Advogado:
    def __init__(self, nome, email, senha, username, cpf, telefone, oab, status = 1):
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.username = username
        self.cpf = cpf
        self.telefone = telefone
        self.oab = oab
        self.status = status 

    @classmethod
    def cadastrar_advogado(cls):
        nome = input('Digite seu nome: ')
        email = input('Digite seu E-mail: ')
        senha = input('Digite sua senha: ')
        username = input('Digite seu username: ')
        cpf = input('Digite seu CPF: ')
        telefone = input('Digite seu número de telefone: ')
        oab = input('Digite o número de registro da sua OAB: ')

        advogado = Advogado(nome, email, senha, username, cpf, telefone, oab)
        return cls(advogado)