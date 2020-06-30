import pygame
from pygame import mixer

# initialize the funcitons in pygame
pygame.init()

# Set up the window and background for the window
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2 hour tutorial: Space Invaders")
icon = pygame.image.load('Art/001-alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Art/space.png')

# Set up clock for FPS
clock = pygame.time.Clock()
FPS = 120

# Grab the size of the screen and set them to variables so we can manipluate them later.
X, Y = pygame.display.get_surface().get_size()
print("game screen canvas size:", X, Y)

# player image
playerIMG = pygame.image.load('Art/002-space-shuttle.png')


def cut_sceen_boss():
    playerY_change = -4
    playerX = X / 2 - 32
    playerY = 664

    # Since we need multiple of the same enemy we will create multiple lists, each position in the list is a new enemy.
    bossIMG = pygame.image.load('Art/mothership.png')
    bossX = 0
    bossY = -100
    bossY_change = 2

    # player function to draw the player to the window.
    def player(x, y):
        win.blit(playerIMG, (x, y))
        return

    # enemy function to draw the enemy to the window.
    def boss(x, y):
        win.blit(bossIMG, (x, y))
        return

    count = 0
    run = True
    while run:
        clock.tick(FPS)
        win.blit(background, (0, 0))

        # Enemy Interactions
        boss(bossX, bossY)
        bossY += bossY_change

        if bossY >= -10:
            bossY = -10
            bossY_change = 0

        # Incrament the player y cordinate
        playerY += playerY_change

        if playerY <= 500:
            playerY = 500
            playerY_change = 0

        count += 1
        if count >= 200:
            break

        player(playerX, playerY)
        pygame.display.update()

    return


# cut_sceen_boss()
