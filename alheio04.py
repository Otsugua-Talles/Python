import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

# ==== FUNÇÕES DE ARQUIVO ====
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

# ==== CLASSE Meetx ====
class MeetxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meetx")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")
        self.usuarios = carregar_usuarios()
        self.tela_login()

    # ==== TELA DE LOGIN ====
    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.root, text="Meetx - Login", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="#00FFAA").pack(pady=15)

        tk.Label(self.root, text="E-mail:", bg="#1e1e1e", fg="white").pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:", bg="#1e1e1e", fg="white").pack()
        self.senha_entry = tk.Entry(self.root, font=("Arial", 12), width=30, show="*")
        self.senha_entry.pack(pady=5)

        tk.Button(self.root, text="Login", bg="#00FFAA", font=("Arial", 12), width=12, command=self.login).pack(pady=10)
        tk.Button(self.root, text="Cadastrar", bg="#5555FF", font=("Arial", 12), width=12, command=self.tela_cadastro).pack()

    # ==== LOGIN ====
    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if email in self.usuarios and self.usuarios[email]["senha"] == senha:
            self.tela_bem_vindo(self.usuarios[email]["nome"])
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos!")

    # ==== TELA DE CADASTRO ====
    def tela_cadastro(self):
        self.limpar_tela()
        tk.Label(self.root, text="Meetx - Cadastro", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="#00FFAA").pack(pady=15)

        tk.Label(self.root, text="Nome:", bg="#1e1e1e", fg="white").pack()
        self.nome_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="E-mail:", bg="#1e1e1e", fg="white").pack()
        self.email_cadastro_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.email_cadastro_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:", bg="#1e1e1e", fg="white").pack()
        self.senha_cadastro_entry = tk.Entry(self.root, font=("Arial", 12), width=30, show="*")
        self.senha_cadastro_entry.pack(pady=5)

        tk.Button(self.root, text="Cadastrar", bg="#00FFAA", font=("Arial", 12), width=12, command=self.cadastrar).pack(pady=10)
        tk.Button(self.root, text="Voltar", bg="#FF5555", font=("Arial", 12), width=12, command=self.tela_login).pack()

    # ==== CADASTRO ====
    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_cadastro_entry.get()
        senha = self.senha_cadastro_entry.get()

        if email in self.usuarios:
            messagebox.showerror("Erro", "E-mail já cadastrado!")
        elif not nome or not email or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            self.usuarios[email] = {"nome": nome, "senha": senha}
            salvar_usuarios(self.usuarios)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.tela_login()

    # ==== TELA BEM-VINDO ====
    def tela_bem_vindo(self, nome):
        self.limpar_tela()
        tk.Label(self.root, text=f"Bem-vindo(a), {nome}!", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="#00FFAA").pack(pady=50)
        tk.Button(self.root, text="Sair", bg="#FF5555", font=("Arial", 12), width=12, command=self.tela_login).pack()

    # ==== LIMPAR TELAS ====
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ==== EXECUÇÃO ====
if __name__ == "__main__":
    root = tk.Tk()
    app = MeetxApp(root)
    root.mainloop()