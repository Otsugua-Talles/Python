import tkinter as tk
import time
import datetime

# Cria a janela principal
janela = tk.Tk()
janela.title("Relógio Digital ⏰")
janela.geometry("350x180")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")

# Cria o rótulo da hora
label_hora = tk.Label(
    janela,
    font=("Arial", 48, "bold"),
    bg="#1e1e1e",
    fg="#00FFAA"
)
label_hora.pack(pady=10)

# Cria o rótulo da data
label_data = tk.Label(
    janela,
    font=("Arial", 18),
    bg="#1e1e1e",
    fg="#FFFFFF"
)
label_data.pack()

# Função para atualizar a hora e a data
def atualizar_relogio():
    agora = datetime.datetime.now()
    hora = agora.strftime("%H:%M:%S")
    data = agora.strftime("%d/%m/%Y")

    # Nome do dia da semana
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia_semana = dias[agora.weekday()]

    # Atualiza os textos
    label_hora.config(text=hora)
    label_data.config(text=f"{dia_semana}, {data}")

    # Atualiza a cada 1 segundo
    janela.after(1000, atualizar_relogio)

# Inicia o relógio
atualizar_relogio()

# Mantém a janela aberta
janela.mainloop()
