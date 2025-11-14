import bcrypt
from models.cliente import Cliente
from models.advogado import Advogado

def criptografar_senha(senha):
    sal = bcrypt.gensalt()
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), sal)
    return senha_criptografada 

def verificar_senha(senha, senha_criptografada):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_criptografada)