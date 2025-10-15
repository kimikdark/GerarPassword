from cryptography.fernet import Fernet
import os

# Caminhos fixos
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CHAVE_PATH = os.path.join(DATA_DIR, 'key.key')
SENHAS_PATH = os.path.join(DATA_DIR, 'passwords.csv')

def obter_fernet():

    #Gera ou carrega a chave de criptografia (Fernet).
    #Se o ficheiro estiver vazio ou inválido, gera uma nova chave.

    os.makedirs(DATA_DIR, exist_ok=True)
    gerar_nova = False

    if not os.path.exists(CHAVE_PATH):
        gerar_nova = True
    else:
        with open(CHAVE_PATH, 'rb') as f:
            chave = f.read()
        try:
            Fernet(chave)  # testa se a chave é válida
        except ValueError:
            gerar_nova = True

    if gerar_nova:
        chave = Fernet.generate_key()
        with open(CHAVE_PATH, 'wb') as f:
            f.write(chave)

    with open(CHAVE_PATH, 'rb') as f:
        chave = f.read()
    return Fernet(chave)

def salvar_senha(site, senha):

    #Salva (de forma criptografada) uma linha 'site,senha' no arquivo CSV.

    fernet = obter_fernet()
    dados = f"{site},{senha}\n".encode()
    criptografado = fernet.encrypt(dados)
    with open(SENHAS_PATH, "ab") as f:
        f.write(criptografado + b"\n")
