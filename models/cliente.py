class Cliente:
    def __init__(self, id, nome, email, senha, username, cpf, telefone, status = 1):
        self.id = id
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

        return cls(nome, email, senha, username, cpf, telefone)
       
    def atualizar_cliente(self):
        novo_nome = input(f'Digite o novo nome ({self.nome}):') or self.nome
        novo_email = input(f'Digite o novo email ({self.email}): ') or self.email
        nova_senha = input(f'Digite a nova senha ({self.senha}): ') or self.senha
        novo_username = input(f'Digite o novo username ({self.username}): ') or self.username
        novo_cpf = input(f'Digite o novo CPF ({self.cpf}): ') or self.cpf
        novo_telefone = input(f'Digite o novo número de telefone ({self.telefone}): ') or self.telefone

        self.nome = novo_nome
        self.email = novo_email
        self.senha = nova_senha
        self.username = novo_username
        self.cpf = novo_cpf
        self.telefone = novo_telefone
