import pygame

# intial instances of pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title logo with caption

pygame.display.set_caption("PyVaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player

player_image = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0

alien_image = pygame.image.load("alien_enemy.png")
alien_x = 370
alien_y = 80
alien_x_change = 0


def player(x, y):
    screen.blit(player_image, (x, y))


def alien(x, y):
    screen.blit(alien_image, (x, y))


# Game Loop

running = True

while running:

    screen.fill((5, 0, 0))

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

    player(player_x, player_y)
    alien(alien_x, alien_y)
    pygame.display.update()
