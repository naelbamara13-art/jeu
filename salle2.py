import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("What's Next? - Room Test")

clock = pygame.time.Clock()

# couleurs
BG = (30, 30, 30)
P1_COLOR = (80, 180, 255)
P2_COLOR = (255, 120, 120)

# joueurs
player1 = pygame.Rect(200, 300, 40, 40)
player2 = pygame.Rect(600, 300, 40, 40)

speed = 4

# porte
door = pygame.Rect(WIDTH - 60, HEIGHT//2 - 40, 50, 80)
DOOR_COLOR = (200, 200, 50)

while True:
    clock.tick(60)
    screen.fill(BG)

    keys = pygame.key.get_pressed()

    # Player 1 (WASD)
    if keys[pygame.K_w]:
        player1.y -= speed
    if keys[pygame.K_s]:
        player1.y += speed
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed

    # Player 2 (flèches)
    if keys[pygame.K_UP]:
        player2.y -= speed
    if keys[pygame.K_DOWN]:
        player2.y += speed
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed

    # limites écran
    player1.clamp_ip(screen.get_rect())
    player2.clamp_ip(screen.get_rect())

    # draw
    pygame.draw.rect(screen, P1_COLOR, player1)
    pygame.draw.rect(screen, P2_COLOR, player2)

# check collision avec la porte
    if player1.colliderect(door) or player2.colliderect(door):
        print("Changement de salle !")
        # Ici tu peux lancer une autre fonction ou changer la salle
        player1.topleft = (100, 300)
        player2.topleft = (700, 300)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()