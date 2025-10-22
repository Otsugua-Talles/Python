import tkinter as tk
import random

# ==== CONFIGURAÇÕES ====
LARGURA = 400
ALTURA = 400
TAMANHO = 20
VEL_INICIAL = 150  # velocidade inicial em ms

# ==== CLASSE COBRA ====
class Cobra:
    def __init__(self, canvas):
        self.canvas = canvas
        self.corpo = [(0, 0)]
        self.direcao = "direita"
        self.rects = []
        self.criar_cobra()
    
    def criar_cobra(self):
        for x, y in self.corpo:
            rect = self.canvas.create_rectangle(x, y, x+TAMANHO, y+TAMANHO, fill="green")
            self.rects.append(rect)
    
    def mover(self):
        x, y = self.corpo[-1]
        if self.direcao == "direita": x += TAMANHO
        elif self.direcao == "esquerda": x -= TAMANHO
        elif self.direcao == "cima": y -= TAMANHO
        elif self.direcao == "baixo": y += TAMANHO
        
        self.corpo.append((x, y))
        rect = self.canvas.create_rectangle(x, y, x+TAMANHO, y+TAMANHO, fill="green")
        self.rects.append(rect)
        self.corpo.pop(0)
        self.canvas.delete(self.rects.pop(0))
    
    def mudar_direcao(self, nova):
        opposites = {"direita":"esquerda", "esquerda":"direita", "cima":"baixo", "baixo":"cima"}
        if nova != opposites[self.direcao]:
            self.direcao = nova
    
    def crescer(self):
        x, y = self.corpo[-1]
        self.corpo.append((x, y))
        rect = self.canvas.create_rectangle(x, y, x+TAMANHO, y+TAMANHO, fill="lime")
        self.rects.append(rect)
    
    def colisao(self):
        x, y = self.corpo[-1]
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA: return True
        if (x, y) in self.corpo[:-1]: return True
        return False
    
    def cabeca(self):
        return self.corpo[-1]

# ==== CLASSE COMIDA ====
class Comida:
    def __init__(self, canvas):
        self.canvas = canvas
        self.posicao = self.gerar_posicao()
        self.rect = self.canvas.create_rectangle(*self.posicao, self.posicao[0]+TAMANHO, self.posicao[1]+TAMANHO, fill="red")
    
    def gerar_posicao(self):
        x = random.randint(0, (LARGURA-TAMANHO)//TAMANHO) * TAMANHO
        y = random.randint(0, (ALTURA-TAMANHO)//TAMANHO) * TAMANHO
        return (x, y)
    
    def reposicionar(self):
        self.canvas.delete(self.rect)
        self.posicao = self.gerar_posicao()
        self.rect = self.canvas.create_rectangle(*self.posicao, self.posicao[0]+TAMANHO, self.posicao[1]+TAMANHO, fill="red")

# ==== CLASSE JOGO ====
class Jogo:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake 2.0")
        self.canvas = tk.Canvas(root, width=LARGURA, height=ALTURA, bg="black")
        self.canvas.pack()

        self.cobra = Cobra(self.canvas)
        self.comida = Comida(self.canvas)
        self.pontuacao = 0
        self.velocidade = VEL_INICIAL

        # Label de pontuação
        self.label_score = tk.Label(root, text=f"Pontuação: {self.pontuacao}", font=("Arial", 14), bg="black", fg="white")
        self.label_score.pack()

        self.root.bind("<Up>", lambda e: self.cobra.mudar_direcao("cima"))
        self.root.bind("<Down>", lambda e: self.cobra.mudar_direcao("baixo"))
        self.root.bind("<Left>", lambda e: self.cobra.mudar_direcao("esquerda"))
        self.root.bind("<Right>", lambda e: self.cobra.mudar_direcao("direita"))

        self.jogo_ativo = True
        self.jogo_loop()

    def jogo_loop(self):
        if self.jogo_ativo:
            self.cobra.mover()

            if self.cobra.colisao():
                self.jogo_ativo = False
                self.canvas.create_text(LARGURA//2, ALTURA//2, text=f"Fim de Jogo 😢\nPontuação: {self.pontuacao}", fill="white", font=("Arial", 24))
                return

            if self.cobra.cabeca() == self.comida.posicao:
                self.cobra.crescer()
                self.comida.reposicionar()
                self.pontuacao += 10
                self.label_score.config(text=f"Pontuação: {self.pontuacao}")
                # Aumenta a velocidade
                self.velocidade = max(50, self.velocidade - 5)

            self.root.after(self.velocidade, self.jogo_loop)

# ==== EXECUÇÃO ====
if __name__ == "__main__":
    root = tk.Tk()
    jogo = Jogo(root)
    root.mainloop()
