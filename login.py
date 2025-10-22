import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import json
import os

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_CHAT = "chat.json"

# ==== FUNÇÕES DE ARQUIVO ====
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def carregar_chat():
    if os.path.exists(ARQUIVO_CHAT):
        with open(ARQUIVO_CHAT, "r") as f:
            return json.load(f)
    return []

def salvar_chat(chat):
    with open(ARQUIVO_CHAT, "w") as f:
        json.dump(chat, f, indent=4)

# ==== CLASSE MeetxApp ====
class MeetxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meetx 4.0")
        self.root.geometry("750x500")
        self.tema = "escuro"
        self.usuarios = carregar_usuarios()
        self.chat = carregar_chat()
        self.usuario_logado = None
        self.tela_login()

    # ==== TEMA ====
    def aplicar_tema(self):
        if self.tema == "escuro":
            self.bg_main = "#2e2e2e"
            self.bg_menu = "#1e1e1e"
            self.fg_texto = "white"
            self.btn_color = "#5555FF"
            self.btn_sair = "#FF5555"
        else:
            self.bg_main = "#f0f0f0"
            self.bg_menu = "#cccccc"
            self.fg_texto = "black"
            self.btn_color = "#0077FF"
            self.btn_sair = "#FF4444"
        self.root.configure(bg=self.bg_main)

    def alternar_tema(self):
        self.tema = "claro" if self.tema == "escuro" else "escuro"
        self.tela_dashboard()

    # ==== LOGIN ====
    def tela_login(self):
        self.limpar_tela()
        self.aplicar_tema()
        tk.Label(self.root, text="Meetx Login", font=("Arial", 24, "bold"), bg=self.bg_main, fg="#00FFAA").pack(pady=20)

        tk.Label(self.root, text="E-mail:", bg=self.bg_main, fg=self.fg_texto).pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:", bg=self.bg_main, fg=self.fg_texto).pack()
        self.senha_entry = tk.Entry(self.root, font=("Arial", 12), width=30, show="*")
        self.senha_entry.pack(pady=5)

        tk.Button(self.root, text="Login", bg="#00FFAA", font=("Arial", 12), width=12, command=self.login).pack(pady=10)
        tk.Button(self.root, text="Cadastrar", bg="#5555FF", font=("Arial", 12), width=12, command=self.tela_cadastro).pack()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        if email in self.usuarios and self.usuarios[email]["senha"] == senha:
            self.usuario_logado = self.usuarios[email]["nome"]
            self.tela_dashboard()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos!")

    # ==== CADASTRO ====
    def tela_cadastro(self):
        self.limpar_tela()
        self.aplicar_tema()
        tk.Label(self.root, text="Meetx - Cadastro", font=("Arial", 24, "bold"), bg=self.bg_main, fg="#00FFAA").pack(pady=15)

        tk.Label(self.root, text="Nome:", bg=self.bg_main, fg=self.fg_texto).pack()
        self.nome_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="E-mail:", bg=self.bg_main, fg=self.fg_texto).pack()
        self.email_cadastro_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.email_cadastro_entry.pack(pady=5)

        tk.Label(self.root, text="Senha:", bg=self.bg_main, fg=self.fg_texto).pack()
        self.senha_cadastro_entry = tk.Entry(self.root, font=("Arial", 12), width=30, show="*")
        self.senha_cadastro_entry.pack(pady=5)

        tk.Button(self.root, text="Cadastrar", bg="#00FFAA", font=("Arial", 12), width=12, command=self.cadastrar).pack(pady=10)
        tk.Button(self.root, text="Voltar", bg="#FF5555", font=("Arial", 12), width=12, command=self.tela_login).pack()

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

    # ==== DASHBOARD ====
    def tela_dashboard(self):
        self.limpar_tela()
        self.aplicar_tema()
        tk.Label(self.root, text=f"Bem-vindo(a), {self.usuario_logado}!", font=("Arial", 20, "bold"), bg=self.bg_main, fg="#00FFAA").pack(pady=10)

        main_frame = tk.Frame(self.root, bg=self.bg_main)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Menu lateral
        menu_frame = tk.Frame(main_frame, bg=self.bg_menu, width=160)
        menu_frame.pack(side="left", fill="y", padx=5, pady=5)
        tk.Button(menu_frame, text="Perfil", bg=self.btn_color, fg="white", width=18, command=lambda:self.mostrar_mensagem("Perfil")).pack(pady=10)
        tk.Button(menu_frame, text="Usuários", bg=self.btn_color, fg="white", width=18, command=self.lista_usuarios).pack(pady=10)
        tk.Button(menu_frame, text="Chat", bg=self.btn_color, fg="white", width=18, command=self.tela_chat).pack(pady=10)
        tk.Button(menu_frame, text="Alternar Tema", bg=self.btn_color, fg="white", width=18, command=self.alternar_tema).pack(pady=10)
        tk.Button(menu_frame, text="Sair", bg=self.btn_sair, fg="white", width=18, command=self.sair).pack(pady=10)

        # Frame de conteúdo
        self.conteudo_frame = tk.Frame(main_frame, bg=self.bg_main)
        self.conteudo_frame.pack(side="right", fill="both", expand=True, padx=10)

        tk.Label(self.conteudo_frame, text="Selecione uma opção no menu lateral", bg=self.bg_main, fg=self.fg_texto, font=("Arial", 14)).pack(pady=50)

    # ==== LISTA DE USUÁRIOS ====
    def lista_usuarios(self):
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
        tk.Label(self.conteudo_frame, text="Usuários cadastrados:", bg=self.bg_main, fg=self.fg_texto, font=("Arial", 16)).pack(pady=10)

        tree = ttk.Treeview(self.conteudo_frame, columns=("Nome", "Email"), show="headings")
        tree.heading("Nome", text="Nome")
        tree.heading("Email", text="E-mail")
        tree.pack(fill="both", expand=True, padx=20, pady=10)

        for email, info in self.usuarios.items():
            tree.insert("", "end", values=(info["nome"], email))

    # ==== CHAT INTERNO COM NOTIFICAÇÕES ====
    def tela_chat(self):
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
        tk.Label(self.conteudo_frame, text="Chat Interno", bg=self.bg_main, fg=self.fg_texto, font=("Arial", 16)).pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(self.conteudo_frame, width=65, height=15, state="disabled", bg=self.bg_menu, fg=self.fg_texto)
        self.chat_area.pack(padx=10, pady=10)
        self.atualizar_chat_area()

        self.msg_entry = tk.Entry(self.conteudo_frame, width=55)
        self.msg_entry.pack(side="left", padx=10, pady=5)
        tk.Button(self.conteudo_frame, text="Enviar", bg="#00FFAA", command=self.enviar_msg).pack(side="left", padx=5, pady=5)

    def atualizar_chat_area(self):
        self.chat_area.configure(state="normal")
        self.chat_area.delete(1.0, tk.END)
        for msg in self.chat:
            self.chat_area.insert(tk.END, f"{msg['usuario']}: {msg['mensagem']}\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.see(tk.END)

    def enviar_msg(self):
        texto = self.msg_entry.get().strip()
        if texto:
            self.chat.append({"usuario": self.usuario_logado, "mensagem": texto})
            salvar_chat(self.chat)
            self.msg_entry.delete(0, tk.END)
            self.atualizar_chat_area()
            messagebox.showinfo("Nova Mensagem", f"{self.usuario_logado} enviou uma nova mensagem!")

    # ==== M
    # ==== MENSAGENS DE MENU ====
    def mostrar_mensagem(self, texto):
        for widget in self.conteudo_frame.winfo_children():
            widget.destroy()
        tk.Label(self.conteudo_frame, text=f"Você selecionou: {texto}", bg=self.bg_main, fg=self.fg_texto, font=("Arial", 16)).pack(pady=50)

    # ==== SAIR ====
    def sair(self):
        self.usuario_logado = None
        self.tela_login()

    # ==== LIMPAR TELAS ====
    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ==== EXECUÇÃO ====
if __name__ == "__main__":
    root = tk.Tk()
    app = MeetxApp(root)
    root.mainloop()
