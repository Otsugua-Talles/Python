import tkinter as tk
import random

# ==== FUNÇÃO DE BOTÕES ====
def botao_nao_seguir_mouse(event):
    # Move o botão "Não" para uma posição aleatória dentro do frame
    x = random.randint(50, 250)
    y = random.randint(150, 250)
    botao_nao.place(x=x, y=y)

def botao_sim_clicado():
    # Oculta os botões e pergunta, e mostra comemoração
    botao_sim.place_forget()
    botao_nao.place_forget()
    pergunta.pack_forget()

    texto_comemorativo = tk.Label(main_frame, text="Finalmente! 🎉🎊✨",
                                  font=("Helvetica", 28, "bold"),
                                  fg="#00CC00", bg="#ffffff")
    texto_comemorativo.pack(pady=60)

    # Efeito de cores piscando
    cores = ["#00CC00", "#FFAA00", "#FF5555", "#00AAFF", "#FF00FF"]
    def animar(ind=0):
        texto_comemorativo.config(fg=cores[ind % len(cores)])
        root.after(300, animar, ind+1)
    animar()

# ==== JANELA PRINCIPAL ====
root = tk.Tk()
root.title("Perguntinha - Estilo Web")
root.geometry("500x400")
root.configure(bg="#e6e6e6")
root.resizable(False, False)

# Frame central estilo "card"
main_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=350)

# Pergunta central
pergunta = tk.Label(main_frame, text="Hoje tem c*?",
                    font=("Helvetica", 24, "bold"),
                    fg="#333333", bg="#ffffff")
pergunta.pack(pady=40)

# Botão Sim com estilo moderno
botao_sim = tk.Button(main_frame, text="Sim", width=12, height=2,
                      bg="#00CCFF", fg="white",
                      font=("Helvetica", 14, "bold"),
                      bd=0, activebackground="#0099CC",
                      command=botao_sim_clicado)
botao_sim.place(x=90, y=180)

# Botão Não com estilo moderno
botao_nao = tk.Button(main_frame, text="Não", width=12, height=2,
                      bg="#FF5555", fg="white",
                      font=("Helvetica", 14, "bold"),
                      bd=0, activebackground="#CC3333",
                      command=lambda: None)
botao_nao.place(x=250, y=180)
botao_nao.bind("<Enter>", botao_nao_seguir_mouse)

# ==== EXECUÇÃO ====
root.mainloop()
