class Cliente:
    def __init__(self, nome, email, senha, username, cpf, telefone, status = 1):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.username = username
        self.cpf = cpf
        self.telefone = telefone
        self.status = status

    @classmethod
    def criar_cliente(cls):
        nome = input('Digite seu nome: ')
        email = input('Digite seu E-mail: ')
        senha = input('Digite sua senha: ')
        username = input('Digite seu username: ')
        cpf = input('Digite seu CPF: ')
        telefone = input('Digite seu número de telefone: ')

        cliente = Cliente(nome, email, senha, username, cpf, telefone)
        return cls(cliente)