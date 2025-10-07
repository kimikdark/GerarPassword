import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória com o tamanho especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def gerar():
    """Lê o tamanho e gera a senha, atualizando o campo de texto."""
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
             messagebox.showwarning("Aviso", "O tamanho deve ser um número positivo!")
             return
        senha = gerar_senha(tamanho)
        # Permite edição temporariamente para inserir o texto
        entry_senha.config(state='normal')
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
        entry_senha.config(state='readonly') # Volta para somente leitura
    except ValueError:
        messagebox.showerror("Erro", "Insira um número inteiro válido para o tamanho!")

# ----------------- Interface com Botão Corrigido -----------------
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")

# --- Cores e Estilos ---
COR_FUNDO = '#F7F7F7'        # Fundo Cinza Muito Claro
COR_TEXTO = '#333333'        # Texto Cinza Escuro
COR_DESTAQUE = '#003366'     # Azul Marinho Escuro (Navy Blue) - PARA O BOTÃO
COR_DESTAQUE_CLIQUE = '#001F3F' # Azul Marinho mais escuro para o efeito de clique
COR_SENHA = '#0056b3'        # Azul Escuro para a senha

janela.configure(bg=COR_FUNDO)

# Configuração de estilo para labels e frames (mantemos ttk para melhor look)
estilo = ttk.Style()
estilo.configure('TFrame', background=COR_FUNDO)
estilo.configure('TLabel', background=COR_FUNDO, foreground=COR_TEXTO, font=('Arial', 10))

# Frame principal com padding
frame_principal = ttk.Frame(janela, padding="20 20 20 20", style='TFrame')
frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

# 1. Entrada do Tamanho
label_tamanho = ttk.Label(frame_principal, text="Tamanho da senha:", style='TLabel')
label_tamanho.grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)

entry_tamanho = tk.Entry(frame_principal, width=10, font=('Arial', 10))
entry_tamanho.insert(0, "12")
entry_tamanho.grid(row=0, column=1, pady=5, padx=5, sticky=(tk.W, tk.E))

# 2. Botão de Gerar - AGORA USANDO tk.Button!
button_gerar = tk.Button(
    frame_principal,
    text="Gerar Senha",
    command=gerar,
    font=('Arial', 10, 'bold'),
    bg=COR_DESTAQUE,           # Fundo Azul Marinho
    fg='white',                # Texto Branco
    activebackground=COR_DESTAQUE_CLIQUE, # Efeito de clique mais escuro
    activeforeground='white',
    relief=tk.FLAT             # Botão plano para look moderno
)
button_gerar.grid(row=1, column=0, columnspan=2, pady=15, sticky=(tk.W, tk.E))

# 3. Saída da Senha
label_senha = ttk.Label(frame_principal, text="Senha gerada:", style='TLabel')
label_senha.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

# O campo da senha
entry_senha = tk.Entry(
    frame_principal,
    width=40,
    font=('Courier', 12, 'bold'),
    fg=COR_SENHA,
    readonlybackground='white',
    insertbackground=COR_TEXTO
)
entry_senha.grid(row=3, column=0, columnspan=2, pady=(0, 5), padx=5, sticky=(tk.W, tk.E))
entry_senha.config(state='readonly')

# Centralização da janela e bloqueio de redimensionamento
janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f'{largura}x{altura}+{x}+{y}')
janela.resizable(False, False)

janela.mainloop()