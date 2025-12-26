import pygame
import sys

pygame.init()

# music :
pygame.mixer.init()
pygame.mixer.music.load("music/music.epic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#display/screen :
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("What's Next?")

clock = pygame.time.Clock()

# colors and fonts :
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (100, 150, 255)
RED = (255, 0, 0)

title_font = pygame.font.SysFont('Arial', 60)
menu_font = pygame.font.SysFont('Arial', 30)

def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, BLUE, rect)
        if click[0]:
            return True
    else:
        pygame.draw.rect(screen, GRAY, rect)

    label = menu_font.render(text, True, WHITE)
    screen.blit(label, (x + 20, y + 10))
    return False


def draw_player_card(x, y, name, connected = True):
    card = pygame.Rect(x, y, 200,  250)
    pygame.draw.rect(screen, (40, 40, 40), card, border_radius=20)

    #cercle pour l'avatar
    avatar_center = (x + 100, y + 70)
    pygame.draw.circle(screen, (90, 90, 90), avatar_center, 45)

    #status de connexion
    status_color = (0, 200, 0) if connected else (200, 0, 0)
    pygame.draw.circle(screen, status_color, (x + 160, y + 20), 8)

    name_text = menu_font.render(name, True, WHITE)
    screen.blit(name_text, (x + 100 - name_text.get_width()//2, y + 140))

    status = "Connecté" if connected else "Déconnecté"
    status_text = menu_font.render(status, True, GRAY)
    screen.blit(status_text, (x + 100 - status_text.get_width()//2, y + 170))



def main_menu():
    global state
    running = True
    current_level = 1

    while running:
        DARK_GRAY = (30, 30, 30)
        screen.fill(DARK_GRAY)
        draw_player_card(150, 200, "Player 1", True)
        draw_player_card(550, 200, "Player 2", True)
        clock.tick(60)
        
        

        title = title_font.render("What's Next?", True, RED)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        pygame.draw.rect(screen, GRAY, (80, 480, 350, 80))
        pygame.draw.rect(screen, GRAY, (470, 480, 350, 80))

        p1 = menu_font.render("JOUEUR 1 CONNECTER", True, BLACK)
        p2 = menu_font.render("JOUEUR 2 CONNECTER", True, BLACK)

        screen.blit(p1, (120, 500))
        screen.blit(p2, (480, 500))

        if draw_button("Nouvelle partie", 300, 250, 250, 80):
            print("Nouvelle partie")

        if draw_button(f"Continuer (Niveau {current_level})", 300, 300, 250, 80):
            print("Continuer")

        if draw_button("Paramètres", WIDTH - 220, 20, 200, 45):
            state = "settings"
            return
        if draw_button("Quitter", 300, 400, 250, 50):
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.flip()

#volume:
volume = 0.5

#button qui glisse:
def draw_slider(x, y, w, value):
    pygame.draw.rect(screen, GRAY, (x, y, w, 6))
    knob_x = x + int(w * value)
    pygame.draw.circle(screen, BLUE, (knob_x, y + 3), 10)

    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        if x <= mx <= x + w and y - 10 <= my <= y + 10:
            return (mx - x)/ w
    return value


#luminosité:
brightness = 0.0

def apply_brightness(level):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(int(level * 180))
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))


#ecran parametres:
def settings_menu():
    global volume, brightness, state

    running = True
    while running:
        clock.tick(60)
        screen.fill((30,30,30))

        title = title_font.render("Settings", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

        vol_text = menu_font.render("Volume", True, WHITE)
        screen.blit(vol_text, (200, 180))
        volume = draw_slider(200, 220, 500, volume)
        pygame.mixer.music.set_volume(volume)

        bri_text = menu_font.render("Brightness", True, WHITE)
        screen.blit(bri_text, (200, 280))
        brightness = draw_slider(200, 320, 500, brightness)

        if draw_button("Back", 350, 420, 200, 60):
            state = "menu"
            return
        
        apply_brightness(brightness)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()

state = "menu"
while True:
    if state == "menu":
        main_menu()
    elif state == "settings":
        settings_menu()
