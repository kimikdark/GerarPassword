import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def gerar():
    try:
        tamanho = int(entry_tamanho.get())
        senha = gerar_senha(tamanho)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Insira um número válido!")

# --- Interface ---
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x200")

tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.insert(0, "12")
entry_tamanho.pack()

tk.Button(janela, text="Gerar Senha", command=gerar).pack(pady=10)

tk.Label(janela, text="Senha gerada:").pack()
entry_senha = tk.Entry(janela, width=40)
entry_senha.pack()

janela.mainloop()
