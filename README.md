# Secure Password Generator

Aplicação Python com interface **Tkinter** que gera senhas aleatórias e as armazena de forma **criptografada**.

## Features
- Password generation with letters, numbers, and symbols.
- Simple and intuitive graphical interface.
- Secure storage in an encrypted `.csv` file.
- Unique encryption key, automatically generated upon first execution.

---

## How to Use

### 1. Open the Project
- Open PyCharm or another Python IDE.
- Go to **`File > Open...`** and select the `gerador_senhas/` folder.

### 2. Create and Configure the Virtual Environment
- In PyCharm:  
  **`File > Settings > Project > Python Interpreter`**  
  Click **➕** → “Add New Virtualenv Environment”.
- Or via terminal:
  ```bash
  python -m venv venv

### 3. Activate the Virtual Environment

- Windows:
   **`venv\Scripts\activate`** 
- MacOS / Linux:
   **`source venv/bin/activate`** 

### 4. Install Dependencies
- In PyCharm: right-click `main.py` → Run 'main'
- Or via terminal:
   **`python main.py`** 

### Important Notes

- The `chave.key` file is essential for decrypting the passwords. Do not delete it, otherwise the saved passwords will become inaccessible.
- The content of `senhas.csv` is not readable, as it is encrypted.
- Before saving each password, make sure to fill in the Site/App Name field.


