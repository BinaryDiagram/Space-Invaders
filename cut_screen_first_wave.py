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


def cut_sceen(playerX, playerY, enemyY, enemyX):
    playerY_change = -4
    # Since we need multiple of the same enemy we will create multiple lists, each position in the list is a new enemy.
    enemyIMG = pygame.image.load('Art/001-alien.png')
    enemyX_change, enemyY_change = [], []
    number_of_enemys = 6

    # This for loop creates all the variables for each enemy.
    # Each enemy needs its own x and y change because of the way the code is writen.
    for i in range(number_of_enemys):
        enemyY_change.append(4)

    # player function to draw the player to the window.
    def player(x, y):
        win.blit(playerIMG, (x, y))
        return

    # enemy function to draw the enemy to the window.
    def enemy(x, y):
        win.blit(enemyIMG, (x, y))
        return

    run = True
    while run:
        clock.tick(FPS)
        win.blit(background, (0, 0))

        # Enemy Interactions
        for i in range(number_of_enemys):
            # Draw each enemy then enemy movement in the x axis
            enemy(enemyX[i], enemyY[i])
            enemyY[i] -= enemyY_change[i]

        # Incrament the player x and y cordinates with the new change from a key press.
        playerY += playerY_change

        if playerY <= -64:
            break

        player(playerX, playerY)
        pygame.display.update()

    return


# cut_sceen(X / 2 - 32, (Y * 4) / 5, [10, 80, 150, 220, 290, 360], [10, 80, 150, 220, 290, 360])
