import pygame
import random

pygame.init()

# --------------------- Configurações ---------------------
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Dinossauro")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = 340
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# --------------------- Dino Pixel Art ---------------------
dino_index = 0
dino_x = 50
vel_y = 0
gravity = 1
jump = -15

# Função para criar sprites do dinossauro
def create_dino_frame(color):
    surface = pygame.Surface((40, 40))
    surface.fill(WHITE)
    pygame.draw.rect(surface, color, (10, 10, 20, 20))
    pygame.draw.rect(surface, color, (12, 30, 6, 6))  # perna esquerda
    pygame.draw.rect(surface, color, (22, 30, 6, 6))  # perna direita
    surface.set_colorkey(WHITE)
    return surface

dino_run1 = create_dino_frame((0, 0, 0))
dino_run2 = create_dino_frame((50, 50, 50))
dino_image = dino_run1

# --------------------- Obstáculos ---------------------
obstacles = []
spawn_timer = 0
cactus_types = [(20, 40), (30, 50), (20, 30, 20)]  # largura, altura ou duplo

# --------------------- Nuvens ---------------------
clouds = []
for _ in range(5):
    clouds.append([random.randint(0, WIDTH), random.randint(50, 150), random.randint(60, 100)])

# --------------------- Botões ---------------------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 255), self.rect)
        draw_text(self.text, font, WHITE, surface, self.rect.centerx, self.rect.centery)
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# --------------------- Funções ---------------------
def draw_text(text, font, color, surface, x, y):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)

def main_game():
    global dino_index, dino_image, vel_y
    # Inicializa elementos do jogo
    dino_rect = dino_image.get_rect(bottom=GROUND_HEIGHT, x=dino_x)
    vel_y = 0
    obstacles = []
    spawn_timer = 0
    score = 0
    anim_counter = 0
    ground_offset = 0
    run = True
    
    while run:
        clock.tick(FPS)
        win.fill((235, 235, 235))
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and dino_rect.bottom == GROUND_HEIGHT:
            vel_y = jump
        
        # Gravidade
        vel_y += gravity
        dino_rect.y += vel_y
        if dino_rect.bottom > GROUND_HEIGHT:
            dino_rect.bottom = GROUND_HEIGHT
            vel_y = 0
        
        # Obstáculos
        spawn_timer += 1
        if spawn_timer > 90:
            spawn_timer = 0
            choice = random.choice(cactus_types)
            if len(choice) == 2:
                w, h = choice
                obstacles.append(pygame.Rect(WIDTH, GROUND_HEIGHT - h, w, h))
            else:  # duplo
                w1, h1, w2 = choice
                obstacles.append(pygame.Rect(WIDTH, GROUND_HEIGHT - h1, w1, h1))
                obstacles.append(pygame.Rect(WIDTH + w1 + 5, GROUND_HEIGHT - h1, w2, h1))
        
        for obs in obstacles[:]:
            obs.x -= 10
            if obs.right < 0:
                obstacles.remove(obs)
                score += 1
            pygame.draw.rect(win, (34, 139, 34), obs)
        
        # Colisão
        for obs in obstacles:
            if dino_rect.colliderect(obs):
                return score
        
        # Nuvens
        for cloud in clouds:
            cloud[0] -= 2
            if cloud[0] + cloud[2] < 0:
                cloud[0] = WIDTH
                cloud[1] = random.randint(50, 150)
                cloud[2] = random.randint(60, 100)
            pygame.draw.ellipse(win, (200, 200, 200), (cloud[0], cloud[1], cloud[2], cloud[2]//2))
        
        # Animação Dino
        anim_counter += 1
        if anim_counter % 10 == 0:
            dino_index = (dino_index + 1) % 2
            dino_image = dino_run1 if dino_index == 0 else dino_run2
        win.blit(dino_image, dino_rect)

        # Pontuação
        draw_text(f"Score: {score}", font, BLACK, win, WIDTH - 100, 30)

        # Chão animado
        ground_offset = (ground_offset - 10) % 40
        for i in range(-1, WIDTH//40 + 2):
            pygame.draw.line(win, BLACK, (i*40 + ground_offset, GROUND_HEIGHT), (i*40 + ground_offset + 20, GROUND_HEIGHT), 2)

        pygame.display.update()

def menu():
    start_btn = Button(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 50, "Iniciar Jogo")
    exit_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 20, 200, 50, "Sair")
    while True:
        win.fill(WHITE)
        draw_text("Jogo do Dinossauro", font, BLACK, win, WIDTH//2, HEIGHT//3)
        start_btn.draw(win)
        exit_btn.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.is_clicked(event.pos):
                    score = main_game()
                    game_over(score)
                if exit_btn.is_clicked(event.pos):
                    pygame.quit()
                    exit()

def game_over(score):
    retry_btn = Button(WIDTH//2 - 100, HEIGHT//2, 200, 50, "Jogar Novamente")
    exit_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 70, 200, 50, "Sair")
    while True:
        win.fill(WHITE)
        draw_text("GAME OVER", font, BLACK, win, WIDTH//2, HEIGHT//3)
        draw_text(f"Sua pontuação: {score}", font, BLACK, win, WIDTH//2, HEIGHT//3 + 50)
        retry_btn.draw(win)
        exit_btn.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.is_clicked(event.pos):
                    score = main_game()
                if exit_btn.is_clicked(event.pos):
                    pygame.quit()
                    exit()

# --------------------- Iniciar Jogo ---------------------
menu()
