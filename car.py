import tkinter as tk
from tkinter import messagebox

# ==== CLASSE CARRO ====
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"{self.modelo} ligado!"
        else:
            return "O carro já está ligado!"

    def desligar(self):
        if self.ligado:
            if self.velocidade > 0:
                return "Desligue o carro somente com velocidade 0!"
            self.ligado = False
            return f"{self.modelo} desligado!"
        else:
            return "O carro já está desligado!"

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            return f"{self.modelo} acelerando! Velocidade: {self.velocidade} km/h"
        else:
            return "Ligue o carro primeiro!"

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            if self.velocidade < 0:
                self.velocidade = 0
            return f"{self.modelo} freando! Velocidade: {self.velocidade} km/h"
        else:
            return "O carro já está parado."


# ==== INTERFACE ====
class AppCarro:
    def __init__(self, root):
        self.carro = Carro("Fusca")

        self.root = root
        self.root.title("Simulador de Carro 🚗")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        # Título
        tk.Label(root, text="🚗 Simulador de Carro", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00FFAA").pack(pady=10)

        # Status
        self.label_status = tk.Label(root, text="Carro desligado", font=("Arial", 14), bg="#1e1e1e", fg="white")
        self.label_status.pack(pady=10)

        # Botões
        tk.Button(root, text="Ligar", bg="#00FFAA", font=("Arial", 12), width=12, command=self.ligar).pack(pady=5)
        tk.Button(root, text="Acelerar", bg="#55AAFF", font=("Arial", 12), width=12, command=self.acelerar).pack(pady=5)
        tk.Button(root, text="Frear", bg="#FFAA00", font=("Arial", 12), width=12, command=self.frear).pack(pady=5)
        tk.Button(root, text="Desligar", bg="#FF5555", font=("Arial", 12), width=12, command=self.desligar).pack(pady=5)

    # Métodos que atualizam a interface
    def atualizar_status(self, mensagem):
        self.label_status.config(text=mensagem)

    def ligar(self):
        msg = self.carro.ligar()
        self.atualizar_status(msg)

    def desligar(self):
        msg = self.carro.desligar()
        self.atualizar_status(msg)

    def acelerar(self):
        msg = self.carro.acelerar()
        self.atualizar_status(msg)

    def frear(self):
        msg = self.carro.frear()
        self.atualizar_status(msg)


# ==== EXECUÇÃO ====
if __name__ == "__main__":
    root = tk.Tk()
    app = AppCarro(root)
    root.mainloop()

