import tkinter as tk
from tkinter import messagebox

# ==== CLASSE MODELO ====
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor


# ==== INTERFACE ====
class AppBanco:
    def __init__(self, root):
        self.conta = ContaBancaria("Talles", 1000.00)

        self.root = root
        self.root.title("Gerenciador Bancário 💰")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        # Título
        tk.Label(root, text="🏦 Conta Bancária", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00FFAA").pack(pady=10)

        # Saldo
        self.label_saldo = tk.Label(root, text=f"Saldo atual: R$ {self.conta.saldo:.2f}", font=("Arial", 14), bg="#1e1e1e", fg="white")
        self.label_saldo.pack(pady=10)

        # Campo de valor
        tk.Label(root, text="Valor:", bg="#1e1e1e", fg="white").pack()
        self.entrada_valor = tk.Entry(root, font=("Arial", 12))
        self.entrada_valor.pack(pady=5)

        # Botões
        tk.Button(root, text="Depositar", bg="#00FFAA", font=("Arial", 12), width=12, command=self.depositar).pack(pady=5)
        tk.Button(root, text="Sacar", bg="#FF5555", font=("Arial", 12), width=12, command=self.sacar).pack(pady=5)
        tk.Button(root, text="Sair", bg="#444444", fg="white", font=("Arial", 12), width=12, command=root.destroy).pack(pady=10)

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo atual: R$ {self.conta.saldo:.2f}")

    def depositar(self):
        try:
            valor = float(self.entrada_valor.get())
            self.conta.depositar(valor)
            self.atualizar_saldo()
            self.entrada_valor.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def sacar(self):
        try:
            valor = float(self.entrada_valor.get())
            self.conta.sacar(valor)
            self.atualizar_saldo()
            self.entrada_valor.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))


# ==== EXECUÇÃO ====
if __name__ == "__main__":
    root = tk.Tk()
    app = AppBanco(root)
    root.mainloop()

