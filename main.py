import tkinter as tk
from tkinter import messagebox
from core import gerar_senha, salvar_senha

def gerar():
    """Gera uma senha e exibe na interface."""
    try:
        tamanho = int(entry_tamanho.get())
        senha = gerar_senha(tamanho)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Insira um número válido para o tamanho da senha.")

def salvar():
    """Salva a senha associada a um site/app no arquivo criptografado."""
    site = entry_site.get().strip()
    senha = entry_senha.get().strip()  # pega senha do campo

    if not site or not senha:
        messagebox.showwarning("Atenção", "Preencha o site e gere a senha antes de salvar.")
        return

    salvar_senha(site, senha)
    messagebox.showinfo("Sucesso", f"Senha para '{site}' salva com sucesso!")
    entry_site.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

# --- Interface Tkinter ---
janela = tk.Tk()
janela.title("🔐 Gerador de Senhas Seguras")
janela.geometry("460x320")

tk.Label(janela, text="Nome do site/app:", font=("Arial", 11)).pack(pady=5)
entry_site = tk.Entry(janela, width=45)
entry_site.pack()

tk.Label(janela, text="Tamanho da senha:", font=("Arial", 11)).pack(pady=5)
entry_tamanho = tk.Entry(janela, width=10, justify="center")
entry_tamanho.insert(0, "12")
entry_tamanho.pack()

tk.Button(janela, text="Gerar Senha", command=gerar, bg="#3B82F6", fg="white").pack(pady=10)

tk.Label(janela, text="Senha gerada:", font=("Arial", 11)).pack()
entry_senha = tk.Entry(janela, width=45)
entry_senha.pack()

tk.Button(janela, text="Salvar Senha", command=salvar, bg="#10B981", fg="white").pack(pady=15)

tk.Label(janela, text="As senhas são armazenadas de forma criptografada.", fg="gray").pack(pady=10)

janela.mainloop()
