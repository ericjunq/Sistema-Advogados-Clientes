class Advogado:
    def __init__(self, id, nome, email, senha, username, cpf, telefone, oab, status = 1):
        self.id = id
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

        return cls(nome, email, senha, username, cpf, telefone, oab)
    
    def atualizar_advogado(self):
        novo_nome = input('Digite o novo nome ({self.nome}): ') or self.nome
        novo_email = input('Digite o novo email ({self.email}): ') or self.email
        nova_senha = input('Digite a nova senha ({self.senha}): ') or self.senha
        novo_username = input('Digite o novo username ({self.username}): ') or self.username
        novo_cpf = input('Digite o novo CPF ({self.cpf}): ') or self.cpf
        novo_telefone = input('Digite o novo número de telefone ({self.telefone}): ') or self.telefone
        nova_oab = input('Digite o novo número de OAB ({self.oab}): ') or self.oab

        self.nome = novo_nome
        self.email = novo_email
        self.senha = nova_senha
        self.username = novo_username
        self.cpf = novo_cpf
        self.telefone = novo_telefone
        self.oab = nova_oab
