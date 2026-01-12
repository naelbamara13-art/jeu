import pygame
import sys

pygame.init()

font = pygame.font.Font(None, 24)
instructions_j1 = "Joueur 1: E pour interagir"
instructions_j2 = "Joueur 2: R pour interagir"



#sizes = pygame.display.get_desktop_sizes()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ma première salle")

#inisialisation des joueurs

#positions
personnage1_pos = [100, 100]
personnage2_pos = [300, 100]
#tailles
personnage1_size = (50, 50)
personnage2_size = (50, 50)
#couleurs
personnage1_color = (0, 128, 255)
personnage2_color = (255, 100, 100)
#vitesses
personnage1_speed = 2
personnage2_speed = 2

# Taille des statues
statue_size = (50, 50)

# Centre de la salle
cx, cy = size[0]//2, size[1]//2
r = 100  # rayon pour espacer les statues

# Création des 4 statues autour du centre
statues = [
    {"nom": "Soleil", "pos": [cx + r, cy], "color": (255, 255, 0), "a": False},      # jaune
    {"nom": "Lune", "pos": [cx - r, cy], "color": (200, 200, 255), "a": False},      # bleu clair
    {"nom": "Racine", "pos": [cx, cy - r], "color": (100, 50, 0), "a": False},       # marron
    {"nom": "Cristal", "pos": [cx, cy + r], "color": (0, 255, 255), "a": False},     # cyan
]

# Ordre correct pour le puzzle
ordre_correct = ["Racine", "Soleil", "Lune"]

# Liste pour stocker les activations
activations = []

# Positions de départ
depart_j1 = [100, 100]
depart_j2 = [300, 100]

personnage1_pos = depart_j1.copy()
personnage2_pos = depart_j2.copy()

puzzle_reussi = False

clock = pygame.time.Clock()

def est_sur_statue(player_pos, player_size, statue_pos, statue_size):
    px, py = player_pos
    pw, ph = player_size
    sx, sy = statue_pos
    sw, sh = statue_size

    # Vérifie si les rectangles se chevauchent
    if (px + pw > sx and px < sx + sw) and (py + ph > sy and py < sy + sh):
        return True
    return False

def reset_puzzle():
    global activations, personnage1_pos, personnage2_pos, puzzle_reussi
    print("Mauvaise statue ! Reset !")
    activations = []
    puzzle_reussi = False
    personnage1_pos = depart_j1.copy()
    personnage2_pos = depart_j2.copy()

    for s in statues:
        s["a"] = False

running = True
while running:
    screen.fill((0, 0, 0))  # fond noir

    # Dessiner les statues (avec couleur dynamique)
    for s in statues:
        if s["a"]:
            color = (100, 255, 100)  # vert = activée
        else:
            color = s["color"]
        pygame.draw.rect(screen, color, (*s["pos"], *statue_size))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Joueur 1 interagit avec E
            if event.key == pygame.K_e:
                for s in statues:
                    if est_sur_statue(personnage1_pos, personnage1_size, s["pos"], statue_size):
                        print(f"Joueur 1 a activé {s['nom']} !")
                        activations.append(s["nom"])
                        # Vérification
                        if activations[-1] != ordre_correct[len(activations)-1]:
                            reset_puzzle()
                        else:
                            s["a"] = True
                            if len(activations) == len(ordre_correct):
                                print("Puzzle réussi !")
                                puzzle_reussi = True
            # Joueur 2 interagit avec R
            if event.key == pygame.K_r:
                for s in statues:
                    if est_sur_statue(personnage2_pos, personnage2_size, s["pos"], statue_size):
                        print(f"Joueur 2 a activé {s['nom']} !")
                        activations.append(s["nom"])
                        # Vérification
                        if activations[-1] != ordre_correct[len(activations)-1]:
                            reset_puzzle()
                        else:
                            s["a"] = True
                            if len(activations) == len(ordre_correct):
                                print("Puzzle réussi !")
                                puzzle_reussi = True
    
    if not puzzle_reussi:
        keys = pygame.key.get_pressed() #detecte les touches appuyees

        # Déplacement joueur 1
        if keys[pygame.K_z]:  # haut
            personnage1_pos[1] -= personnage1_speed
        if keys[pygame.K_s]:  # bas
            personnage1_pos[1] += personnage1_speed
        if keys[pygame.K_q]:  # gauche
            personnage1_pos[0] -= personnage1_speed
        if keys[pygame.K_d]:  # droite
            personnage1_pos[0] += personnage1_speed

        # Déplacement joueur 2
        if keys[pygame.K_UP]:
            personnage2_pos[1] -= personnage2_speed
        if keys[pygame.K_DOWN]:
            personnage2_pos[1] += personnage2_speed
        if keys[pygame.K_LEFT]:
            personnage2_pos[0] -= personnage2_speed
        if keys[pygame.K_RIGHT]:
            personnage2_pos[0] += personnage2_speed
    
    #limites les positions des jouers aux bords de l'ecran
    personnage1_pos[0] = max(0, min(personnage1_pos[0], size[0]-personnage1_size[0]))
    personnage1_pos[1] = max(0, min(personnage1_pos[1], size[1]-personnage1_size[1]))
    personnage2_pos[0] = max(0, min(personnage2_pos[0], size[0]-personnage2_size[0]))
    personnage2_pos[1] = max(0, min(personnage2_pos[1], size[1]-personnage2_size[1]))
    
    # Dessiner les joueurs
    pygame.draw.rect(screen, personnage1_color, (*personnage1_pos, *personnage1_size))
    pygame.draw.rect(screen, personnage2_color, (*personnage2_pos, *personnage2_size))

    
    # Actualiser l'affichage
    pygame.display.flip()
    clock.tick(60) # Limiter à 60 FPS


pygame.quit()
sys.exit()
