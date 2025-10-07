# Pacote principal com as funções de geração e criptografia de senhas.

from .gerador import gerar_senha
from .criptografia import salvar_senha

__all__ = ["gerar_senha", "salvar_senha"]
