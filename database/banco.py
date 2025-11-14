import sqlite3
from models.cliente import Cliente
from models.advogado import Advogado

DB_PATH = 'banco.db'

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela_cliente():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        username TEXT UNIQUE NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        telefone TEXT UNIQUE NOT NULL,
        status INTEGER DEFAULT 1)
    ''', )

def inserir_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes(nome, email, username, cpf, telefone, status)', (cliente.nome, cliente.email, cliente.username, cliente.cpf, cliente.telefone, cliente.status))
    conn.commit()
    conn.close()

def atualizar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''UPDATE clientes
    SET nome = ?,
        email = ?,
        username = ?,
        cpf = ?,
        telefone = ?
    WHERE id = ?
         ''', (cliente.nome, cliente.email, cliente.username, cliente.cpf, cliente.telefone))
    
    conn.commit()
    conn.close()
    

def criar_tabela_advogado():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS advogados(
            id PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            cpf TEXT UNIQUE NOT NULL,     
            telefone TEXT UNIQUE NOT NULL,
            oab TEXT UNIQUE NOT NULL,
            status INTEGER DEFAULT 1)
    ''',)

def inserir_advogado(advogado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO advogados (nome, email, username, cpf, telefone, oab, status)', (advogado.nome, advogado.email, advogado.username, advogado.cpf, advogado.telefone, advogado.oab, advogado.status))
    conn.commit()
    conn.close()

def atualizar_advogado(advogado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(''' UPDATE advogados
        SET nome = ?,
            email = ?,
            username = ?,
            cpf = ?,
            telefone = ?,
            oab = ?
        WHERE id = ?
    ''', (advogado.nome, advogado.email, advogado.username, advogado.cpf, advogado.telefone, advogado.oab))
