#!/usr/bin/python3

from random import randrange
import pygame
from pygame import mixer
import random
import math

# intial instances of pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Add background image

background = pygame.image.load("assests/mountains03-1920-x-1080_full.png")

# Background Music

#mixer.music.load("assests/Dark Fantasy Studio - Particle voyager.mp3")
#mixer.music.play(-1)

# Title logo with caption

pygame.display.set_caption("assests/PyVaders")
icon = pygame.image.load("assests/alien.png")
pygame.display.set_icon(icon)

# Player

player_image = pygame.image.load("assests/darkgrey_02.png")
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
    alien_image.append(pygame.image.load("assests/alien_enemy.png"))
    alien_x.append(random.randrange(0, 800))
    alien_y.append(random.randrange(50, 150))
    alien_x_change.append(0.3)
    alien_y_change.append(30)

# Alien Enemy
laser_image = pygame.image.load("assests/laser.png")
laser_x = 0
laser_y = 500
laser_x_change = 0
laser_y_change = 5
laser_state = "ready"

# Score values
score = 0

# font for score
font = pygame.font.Font("assests/Monoton-Regular.ttf", 32)
score_displayX = 6
score_displayY = 6

# font for Game Over
over_font = pygame.font.Font("assests/Monoton-Regular.ttf", 32)

"""
Draw Function from pygames
Using the screen blit

def player, alien, collision and laser
"""


def show_score(x, y):
    score_display = font.render("Score : " + str(score), True, (255, 0, 0))
    screen.blit(score_display, (x, y))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))

def player(x, y):
    screen.blit(player_image, (x, y))


def alien(x, y, i):
    screen.blit(alien_image[i], (x, y))


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
                player_x_change = -0.5
                # print("Left Key is press")
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
                # print("Right Key is press")
            if event.key == pygame.K_SPACE:
                laser_sound = mixer.Sound("assests/laser.wav")
                laser_sound.play()
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
    """
    interate from a number aliens and generat them
    also check and call isCollision
    """
    for i in range(num_of_enemies):

        # Game Over
        if alien_y[i] > 200:
            for j in range(num_of_enemies):
                alien_y[j] = 2000
            game_over()
            break

        alien_x[i] += alien_x_change[i]

        if alien_x[i] <= 0:
            alien_x_change[i] = 1
            alien_y[i] += alien_y_change[i]

        elif alien_x[i] >= 736:
            alien_x_change[i] = -1
            alien_y[i] += alien_y_change[i]

        collision = isCollision(alien_x[i], alien_y[i], laser_x, laser_y)

        if collision:
            explosion = mixer.Sound("assests/Explosion.wav")
            explosion.play()
            laser_y = 400
            laser_state = "ready"
            score += 1
            alien_x[i] = random.randint(0, 800)
            alien_y[i] = random.randint(50, 150)

        alien(alien_x[i], alien_y[i], i)

    # laser movement
    if laser_y <= 0:
        laser_y = 500
        laser_state = "ready"

    if laser_state is "fire":
        shoot_laser(laser_x, laser_y)
        laser_y -= laser_y_change

    # Call instances

    player(player_x, player_y)

    show_score(score_displayX, score_displayY)

    """
    Final draw call for the game.
    call update by end of loop
    need to keep in the bottom of loop
    """
    pygame.display.update()
