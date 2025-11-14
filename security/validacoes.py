import re

def validar_email(email:str) -> bool():
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_cpf(cpf:str) -> bool():
    cpf = re.sub(r'\D', '', cpf)
    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * 11:
        return False 

    for i in range (9,11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True

def validar_telefone(telefone:str) -> bool():
    telefone = re.sub(r'\D', '', telefone)
    if not telefone.isdigit():
        return False 

    padrao = r'^(?:\+?55)?(?:\d{2})?(?:9\d{8}|\d{8})$'
    return re.match(padrao, telefone) is not None
