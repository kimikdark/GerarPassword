# Secure Password Generator

Aplicação Python com interface **Tkinter** que gera senhas aleatórias e as armazena de forma **criptografada**.

## Features
- Password generation with letters, numbers, and symbols.
- Simple and intuitive graphical interface.
- Secure storage in an encrypted `.csv` file.
- Unique encryption key automatically generated on first run.

---

## How to Use

### 1. Open the Project
- Open PyCharm or another Python IDE.
- Go to **`File > Open...`** and select the `secure_password_generator/` folder.

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

- The file `key.key` is essential to decrypt your stored passwords.
Do not delete or modify it — otherwise, previously saved passwords will become inaccessible.
- The file `passwords.csv` contains encrypted data and is not human-readable.
- Before saving each password, make sure to fill in the Site/App Name field.
- A future update will include a feature to view and manage saved passwords directly from the interface.



