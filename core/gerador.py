import random
import string

def gerar_senha(tamanho=12):

    #Gera uma senha aleatória com letras, números e símbolos.

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))
