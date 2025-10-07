# 🔐 Gerador de Senhas Seguras

Aplicação Python com interface **Tkinter** que gera senhas aleatórias e as armazena de forma **criptografada**.

## ✨ Funcionalidades
- Geração de senhas com letras, números e símbolos.
- Interface gráfica simples e intuitiva.
- Armazenamento seguro em ficheiro `.csv` criptografado.
- Chave de criptografia única, gerada automaticamente na primeira execução.

---

## ⚙️ Como Usar

### 1. Abrir o projeto
- Abra o PyCharm ou outro IDE Python.
- Vá a **`File > Open...`** e selecione a pasta `gerador_senhas/`.

### 2. Criar e configurar o ambiente virtual
- No PyCharm:  
  **`File > Settings > Project > Python Interpreter`**  
  Clique em **➕** → “Add New Virtualenv Environment”.
- Ou via terminal:
  ```bash
  python -m venv venv

### 3. Ativar o ambiente virtual

- Windows:
   **`venv\Scripts\activate`** 
- MacOS / Linux:
   **`source venv/bin/activate`** 

### 4. Instalar dependências
- No PyCharm: clique com o botão direito em main.py → Run 'main'
- Ou via terminal:
   **`python main.py`** 

### Notas Importantes

- O ficheiro chave.key é essencial para desencriptar as senhas. Não o apague, caso contrário as senhas guardadas ficarão inacessíveis.
- O conteúdo de senhas.csv não é legível, pois está criptografado.
- Antes de guardar cada senha, certifique-se de preencher o campo Nome do site/app.


