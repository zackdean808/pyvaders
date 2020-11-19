from random import randrange
import pygame
import random

# intial instances of pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Add background image

background = pygame.image.load("mountains03-1920-x-1080_full.png")

# Title logo with caption

pygame.display.set_caption("PyVaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player

player_image = pygame.image.load("darkgrey_02.png")
player_x = 370
player_y = 480
player_x_change = 0

# Alien Enemy
alien_image = []
alien_x = []
alien_y = []
alien_x_change = []
alien_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    alien_image.append(pygame.image.load("alien_enemy.png"))
    alien_x.append(random.randrange(0, 800))
    alien_y.append(random.randrange(50, 150))
    alien_x_changea.append(0.3)
    alien_y_change.append(30)

# Alien Enemy
laser_image = pygame.image.load("laser.png")
laser_x = 0
laser_y = 500
laser_x_change = 0
laser_y_change = 1
laser_state = "ready"

"""
Draw Function from pygames
Using the screen blit
"""


def player(x, y):
    screen.blit(player_image, (x, y))


def alien(x, y):
    screen.blit(alien_image, (x, y))


def shoot_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser_image, (x + 9, y + 6))


def isCollision(alien_x, alien_y, laser_x, laser_y):
    distance = math.sqrt(
        math.pow(alien_x - laser_x, 2) + math.pow(alien_y - laser_y, 2)
    )
    if distance < 27:
        return True
    else:
        return False


# Game Loop

running = True

while running:

    screen.fill((5, 0, 0))

    screen.blit(background, (0, 0))

    # Listening to each events for key press directions

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
                # print("Left Key is press")
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
                # print("Right Key is press")
            if event.key == pygame.K_SPACE:
                laser_x = player_x
                shoot_laser(laser_x, laser_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Draw with the following colors
    # screen.fill((5, 0, 0))

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0

    elif player_x >= 736:
        player_x = 736

    # Alien movements and x changes position
    alien_x += alien_x_change

    if alien_x <= 0:
        alien_x_change = 0.3
        alien_y += alien_y_change

    elif alien_x >= 736:
        alien_x_change = -0.3
        alien_y += alien_y_change

    # laser movement
    if laser_y <= 0:
        laser_y = 500
        laser_state = "ready"

    if laser_state is "fire":
        shoot_laser(laser_x, laser_y)
        laser_y -= laser_y_change

    # Call instances

    player(player_x, player_y)
    alien(alien_x, alien_y)

    """
    Final draw call for the game.
    """
    pygame.display.update()
