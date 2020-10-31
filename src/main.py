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


def player():
    screen.blit(player_image, (player_x, player_y))


# Game Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw with the following colors
    # screen.fill((5, 0, 0))
    player()
    pygame.display.update()
