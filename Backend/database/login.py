from banco import conectar
from security.criptografar_senha import verificar_senha

def login_advogado(login_dgtd, senha_dgtd):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, nome, email, senha, username, status
        FROM advogados
        WHERE email = ? OR username = ?
        ''', (login_dgtd, login_dgtd))
    
    dados = cursor.fetchone
    conn.close()

    if dados is None:
        return None, 'Conta não encontrada!'
    
    (id, nome, email, senha_criptografada, username, status) = dados

    if status == 0:
        return None, 'Conta inativa!'
    
    if not verificar_senha(senha_dgtd, senha_criptografada):
        return None, "Senha incorreta!"
    
    return {
        'id': id,
        'nome': nome,
        'email': email,
        'username': username,
        'status': status 
    }, f'Login realizado com sucesso. Seja bem vindo {nome}!'

def login_cliente(login_dgtd, senha_dgtd):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, nome, email, senha, username, status
        FROM clientes
        WHERE email = ? OR username = ?
        ''', (login_dgtd, login_dgtd))
    
    dados = cursor.fetchone()
    conn.close()

    if dados is None:
        return None, 'Conta não encontrada!'
    
    (id, nome, email, senha_criptografada, username, status) = dados

    if status == 0:
        return None, 'Conta inativa!'
    
    if not verificar_senha(senha_dgtd, senha_criptografada):
        return None, "Senha incorreta!"
    
    return {
        'id': id,
        'nome': nome,
        'email': email,
        'username': username,
        'status': status 
    }, f'Login realizado com sucesso. Seja bem vindo {nome}!'
    