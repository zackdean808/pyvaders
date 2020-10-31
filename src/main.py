import pygame

# intial instances of pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title Logo

pygame.display.set_caption("PyVaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Game Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw with the following colors
    screen.fill((5, 0, 0))
    pygame.display.update()
