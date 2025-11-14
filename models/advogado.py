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
        nome = input(f'Digite seu nome: ')
        email = input(f'Digite seu E-mail: ')
        senha = input(f'Digite sua senha: ')
        username = input(f'Digite seu username: ')
        cpf = input(f'Digite seu CPF: ')
        telefone = input(f'Digite seu número de telefone: ')
        oab = input(f'Digite o número de registro da sua OAB: ')

        advogado = Advogado(nome, email, senha, username, cpf, telefone, oab)

        return cls(advogado)
