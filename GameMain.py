import pygame
import sys
import random
import math
from pygame import mixer
import time

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


# The main game function that we will call at the Intro_Screen.
def game_main():
    start = time.time()
    enemy_laser_start = time.time()

    # This does not work because it only randomly draws one number it wont exicute more than once out side of a loop.
    # randomX_placement = random.randint(1, (X - 65))

    # Set up the player variables for position and change.
    playerX, playerY = X / 2 - 32, (Y * 4) / 5
    playerX_change, playerY_change, player_vel = 0, 0, 5

    # Since we need multiple of the same enemy we will create multiple lists, each position in the list is a new enemy.
    enemyIMG = pygame.image.load('Art/001-alien.png')
    enemyX, enemyY, enemyX_change, enemyY_change = [], [], [], []
    enemyY_placement = (Y / 15) + 1
    number_of_enemys = 6

    # This for loop creates all the variables for each enemy.
    # Each enemy needs its own x and y change because of the way the code is writen.
    for i in range(number_of_enemys):
        # random placing
        enemyX.append(random.randint(1, (X - 65)))
        enemyY.append(enemyY_placement)
        enemyX_change.append(5)
        enemyY_change.append(50)

    # laser object setup.
    laserIMG = pygame.image.load('Art/laser.png')
    laser_sound = mixer.Sound('SFX/laser.wav')
    laserX, laserY, laser_state = [], [], []
    laserY_change, max_lasers, hide_laser = 10, 10, 1000

    for i in range(max_lasers):
        laserX.append(hide_laser)
        laserY.append(hide_laser)
        laser_state.append("ready")

    # Shotgun Power Up
    shotgun_power_upIMG = pygame.image.load('Art/shotgun.png')
    shotgun_powerX = random.randint(1, (X - 65))
    shotgun_powerY, shotgun_power_change, upgrade_poweroff = 0, 2, 0

    shotgun_state, shotgun_drop = False, False

    # left_Shotgun Laser
    left_shotgunX_laser, left_shotgunY_laser, left_shotgun_laser_state = [], [], []
    left_shotgunY_laser_change, left_shotgunX_laser_change, left_max_shotgun_lasers = 10, 5, 10

    for i in range(left_max_shotgun_lasers):
        left_shotgunX_laser.append(hide_laser)
        left_shotgunY_laser.append(hide_laser)
        left_shotgun_laser_state.append("ready")

    # center_Shotgun Laser
    center_shotgunX_laser, center_shotgunY_laser, center_shotgun_laser_state = [], [], []
    center_shotgunY_laser_change, center_max_shotgun_lasers = 10, 10

    for i in range(center_max_shotgun_lasers):
        center_shotgunX_laser.append(hide_laser)
        center_shotgunY_laser.append(hide_laser)
        center_shotgun_laser_state.append("ready")

    # right_Shotgun Laser
    right_shotgunX_laser, right_shotgunY_laser, right_shotgun_laser_state = [], [], []
    right_shotgunY_laser_change, right_shotgunX_laser_change, right_max_shotgun_lasers = 10, 5, 10

    for i in range(right_max_shotgun_lasers):
        right_shotgunX_laser.append(hide_laser)
        right_shotgunY_laser.append(hide_laser)
        right_shotgun_laser_state.append("ready")

    # Enemy Lasers
    enemy_laserIMG = pygame.image.load('Art/enemy_laser.png')
    enemy_laser_sound = mixer.Sound('SFX/enemy_laser.wav')
    enemy_laserX, enemy_laserY, enemy_laser_state = [], [], []
    enemy_laserY_change, max_enemy_lasers = 5, 6

    for laser in range(max_enemy_lasers):
        enemy_laserX.append(hide_laser)
        enemy_laserY.append(hide_laser)
        enemy_laser_state.append("ready")

    # score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX, textY = 10, 10

    def game_over_text(x, y):
        game_over_font = pygame.font.Font('freesansbold.ttf', 64)
        game_over = game_over_font.render("Game Over", True, (255, 0, 0))
        win.blit(game_over, (x, y))
        return

    def show_score(x, y):
        score = font.render("Score: " + str(score_value), True, (255, 255, 255))
        win.blit(score, (x, y))
        return

    # player function to draw the player to the window.
    def player(x, y):
        win.blit(playerIMG, (x, y))
        return

    # enemy function to draw the enemy to the window.
    def enemy(x, y):
        win.blit(enemyIMG, (x, y))
        return

    def enemy_laser(x, y):
        win.blit(enemy_laserIMG, (x, y))
        return

    def fire_laser(x, y):
        win.blit(laserIMG, (x + 16, y + 10))
        return

    def shotgun_powerup(x, y):
        win.blit(shotgun_power_upIMG, (x, y))
        return

    def left_shotgun_blast(x, y):
        win.blit(laserIMG, (x + 16, y + 15))
        return

    def center_shotgun_blast(x, y):
        win.blit(laserIMG, (x + 16, y + 15))
        return

    def right_shotgun_blast(x, y):
        win.blit(laserIMG, (x + 16, y + 15))
        return

    def character_is_collision(ex, ey, lx, ly):
        distance = math.sqrt((math.pow((ex + 32)-(lx + 32), 2)) + (math.pow((ey + 32)-(ly + 32), 2)))
        if distance < 60:
            return True
        else:
            return False

    def player_laser_is_collision(ex, ey, lx, ly):
        distance = math.sqrt((math.pow((ex + 16)-(lx + 32), 2)) + (math.pow((ey + 16)-(ly + 32), 2)))
        if distance < 40:
            return True
        else:
            return False

    def enemy_laser_upgrade_is_collision(ex, ey, lx, ly):
        distance = math.sqrt((math.pow((ex + 8)-(lx + 32), 2)) + (math.pow((ey + 8)-(ly + 32), 2)))
        if distance < 40:
            return True
        else:
            return False

    run = True
    while run:
        clock.tick(FPS)
        win.blit(background, (0, 0))

        # Timer for upgrade drop
        upgrade_timer = (time.time() - start)
        if upgrade_timer >= 5:
            shotgun_drop = True
            shotgun_powerup(shotgun_powerX, shotgun_powerY)
            # print("current time: ", upgrade_timer)
            start = time.time()

        # Timer for the upgrade to wear off
        upgrade_poweroff_timer = (time.time() - upgrade_poweroff)
        if upgrade_poweroff_timer >= 2.5:
            shotgun_state = False

        # Timer for when the enemys will shoot
        enemy_laser_timer = (time.time() - enemy_laser_start)
        if enemy_laser_timer >= 3:
            enemy_laser_sound.play()
            for i in range(max_enemy_lasers):
                # print("enemy Fire")
                enemy_laserX[i] = enemyX[i]
                enemy_laserY[i] = enemyY[i]
                enemy_laser_state[i] = "fired"
                enemy_laser_start = time.time()

        # Player Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
        # key controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # print("Left Arrow Key Pressed.")
                    playerX_change = -player_vel
                if event.key == pygame.K_RIGHT:
                    # print("Right Arrow Key Pressed.")
                    playerX_change = player_vel
                if event.key == pygame.K_UP:
                    # print("Up Arrow Key Pressed.")
                    playerY_change = -player_vel
                if event.key == pygame.K_DOWN:
                    # print("Down Arrow Key Pressed.")
                    playerY_change = player_vel
                if event.key == pygame.K_SPACE:
                    if shotgun_state:
                        for i in range(left_max_shotgun_lasers):
                            if left_shotgun_laser_state[i] == "ready":
                                # We only need one sound for the shotgun blast
                                laser_sound.play()
                                left_shotgunX_laser[i] = playerX
                                left_shotgunY_laser[i] = playerY
                                left_shotgun_blast(left_shotgunX_laser[i], left_shotgunY_laser[i])
                                left_shotgun_laser_state[i] = "fired"
                                break
                        for i in range(right_max_shotgun_lasers):
                            if right_shotgun_laser_state[i] == "ready":
                                right_shotgunX_laser[i] = playerX
                                right_shotgunY_laser[i] = playerY
                                right_shotgun_blast(right_shotgunX_laser[i], right_shotgunY_laser[i])
                                right_shotgun_laser_state[i] = "fired"
                                break
                        for i in range(center_max_shotgun_lasers):
                            if center_shotgun_laser_state[i] == "ready":
                                center_shotgunX_laser[i] = playerX
                                center_shotgunY_laser[i] = playerY
                                center_shotgun_blast(center_shotgunX_laser[i], center_shotgunY_laser[i])
                                center_shotgun_laser_state[i] = "fired"
                                break
                    # If there are no powerups affecting the player revert the weapon back to the basic laser.
                    else:
                        for j in range(max_lasers):
                            if laser_state[j] == "ready":
                                laser_sound.play()
                                laserX[j] = playerX
                                laserY[j] = playerY
                                # print("Space Bar Pressed.")
                                fire_laser(laserX[j], laserY[j])
                                laser_state[j] = "fired"
                                break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # print("Left or Right arrow was released")
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # print("Left or Right arrow was released")
                    playerY_change = 0

        # Shotgun upgrade collision
        shotgun_player_collision = enemy_laser_upgrade_is_collision(shotgun_powerX, shotgun_powerY, playerX, playerY)
        if shotgun_player_collision:
            shotgun_powerX = random.randint(1, (X - 65))
            shotgun_powerY = 0
            shotgun_drop = False
            shotgun_state = True
            upgrade_poweroff = time.time()

        # Enemy Interactions
        for i in range(number_of_enemys):
            # Draw each enemy then enemy movement in the x axis
            enemy(enemyX[i], enemyY[i])
            enemyX[i] += enemyX_change[i]

            # Enemey boundry check.
            if enemyX[i] <= 0:
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            if enemyX[i] >= (X - 64):
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            if enemyY[i] >= (Y - 32):
                enemyY[i] = enemyY_placement
                enemyX[i] = random.randint(1, (X - 65))

            # Player Collision with Enemy
            player_collision = character_is_collision(enemyX[i], enemyY[i], playerX, playerY)
            if player_collision:
                for j in range(number_of_enemys):
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    game_over_text(((X / 2) - 160), ((Y / 2) - 50))
                    run = False
                break

            # left_Shotgun Laser Collision with Enemy
            for left_shotgun_laser in range(left_max_shotgun_lasers):
                left_shotgun_damage_collision = player_laser_is_collision(left_shotgunX_laser[left_shotgun_laser],
                                                                          left_shotgunY_laser[left_shotgun_laser],
                                                                          enemyX[i], enemyY[i],)
                if left_shotgun_damage_collision:
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    # number_of_enemys += 1
                    left_shotgunX_laser[left_shotgun_laser] = hide_laser
                    left_shotgunY_laser[left_shotgun_laser] = hide_laser
                    left_shotgun_laser_state[left_shotgun_laser] = "ready"
                    score_value += 1
                    # print(score_value)
                    enemyX[i] = random.randint(0, (X - 65))
                    enemyY[i] = (Y * 1) / 15

            # center_Shotgun Laser Collision with Enemy
            for center_shotgun_laser in range(center_max_shotgun_lasers):
                center_shotgun_damage_collision = player_laser_is_collision(center_shotgunX_laser[center_shotgun_laser],
                                                              center_shotgunY_laser[center_shotgun_laser],
                                                                            enemyX[i], enemyY[i])
                if center_shotgun_damage_collision:
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    # number_of_enemys += 1
                    center_shotgunX_laser[center_shotgun_laser] = hide_laser
                    center_shotgunY_laser[center_shotgun_laser] = hide_laser
                    center_shotgun_laser_state[center_shotgun_laser] = "ready"
                    score_value += 1
                    # print(score_value)
                    enemyX[i] = random.randint(0, (X - 65))
                    enemyY[i] = (Y * 1) / 15

            # right_Shotgun Laser Collision with Enemy
            for right_shotgun_laser in range(right_max_shotgun_lasers):
                right_shotgun_damage_collision = player_laser_is_collision(right_shotgunX_laser[right_shotgun_laser],
                                                             right_shotgunY_laser[right_shotgun_laser],
                                                                           enemyX[i], enemyY[i])
                if right_shotgun_damage_collision:
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    # number_of_enemys += 1
                    right_shotgunX_laser[right_shotgun_laser] = hide_laser
                    right_shotgunY_laser[right_shotgun_laser] = hide_laser
                    right_shotgun_laser_state[right_shotgun_laser] = "ready"
                    score_value += 1
                    # print(score_value)
                    enemyX[i] = random.randint(0, (X - 65))
                    enemyY[i] = (Y * 1) / 15

            # player Laser Collision with Enemy
            for single_laser in range(max_lasers):
                collision = player_laser_is_collision(laserX[single_laser], laserY[single_laser], enemyX[i], enemyY[i])
                if collision:
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    # number_of_enemys += 1
                    laserX[single_laser]  = hide_laser
                    laserY[single_laser] = hide_laser
                    laser_state[single_laser] = "ready"
                    score_value += 1
                    # print(score_value)
                    enemyX[i] = random.randint(0, (X - 65))
                    enemyY[i] = (Y * 1) / 15

            # Enemy Laser Collision with Player
            for i in range(max_enemy_lasers):
                enemy_laser_collision = enemy_laser_upgrade_is_collision(enemy_laserX[i], enemy_laserY[i], playerX, playerY)
                if enemy_laser_collision:
                    explosion_sound = mixer.Sound('SFX/explosion.wav')
                    explosion_sound.play()
                    game_over_text(((X / 2) - 160), ((Y / 2) - 50))
                    run = False
                    break

        # left_Shotgun Laser movement
        for left_shotgun_laser in range(left_max_shotgun_lasers):
            if left_shotgun_laser_state[left_shotgun_laser] == "fired":
                left_shotgun_blast(left_shotgunX_laser[left_shotgun_laser], left_shotgunY_laser[left_shotgun_laser])
                left_shotgunY_laser[left_shotgun_laser] -= left_shotgunY_laser_change
                left_shotgunX_laser[left_shotgun_laser] -= left_shotgunX_laser_change
            if left_shotgunY_laser[left_shotgun_laser] <= 0:
                left_shotgun_laser_state[left_shotgun_laser] = "ready"
                left_shotgunY_laser[left_shotgun_laser] = hide_laser
                left_shotgunX_laser[left_shotgun_laser] = hide_laser

        # center_Shotgun Laser movement
        for center_shotgun_laser in range(center_max_shotgun_lasers):
            if center_shotgun_laser_state[center_shotgun_laser] == "fired":
                center_shotgun_blast(center_shotgunX_laser[center_shotgun_laser],
                                     center_shotgunY_laser[center_shotgun_laser])
                center_shotgunY_laser[center_shotgun_laser] -= center_shotgunY_laser_change
            if center_shotgunY_laser[center_shotgun_laser] <= 0:
                center_shotgun_laser_state[center_shotgun_laser] = "ready"
                center_shotgunY_laser[center_shotgun_laser] = hide_laser
                center_shotgunX_laser[center_shotgun_laser] = hide_laser

        # right_Shotgun Laser movement
        for right_shotgun_laser in range(right_max_shotgun_lasers):
            if right_shotgun_laser_state[right_shotgun_laser] == "fired":
                right_shotgun_blast(right_shotgunX_laser[right_shotgun_laser],
                                    right_shotgunY_laser[right_shotgun_laser])
                right_shotgunY_laser[right_shotgun_laser] -= right_shotgunY_laser_change
                right_shotgunX_laser[right_shotgun_laser] += right_shotgunX_laser_change
            if right_shotgunY_laser[right_shotgun_laser] <= 0:
                right_shotgun_laser_state[right_shotgun_laser] = "ready"
                right_shotgunY_laser[right_shotgun_laser] = hide_laser
                right_shotgunX_laser[right_shotgun_laser] = hide_laser

        # Laser movement
        for k in range(max_lasers):
            if laser_state[k] == "fired":
                fire_laser(laserX[k], laserY[k])
                laserY[k] -= laserY_change
            if laserY[k] <= -64:
                laser_state[k] = "ready"
                laserY[k] = hide_laser
                laserX[k] = hide_laser

        # Enemy laser movement and reset
        for i in range(number_of_enemys):
            if enemy_laser_state[i] == "fired":
                enemy_laser(enemy_laserX[i], enemy_laserY[i])
                enemy_laserY[i] += enemy_laserY_change
            if enemy_laserY[i] >= 600:
                enemy_laser_state[i] == "ready"
                enemy_laserY[i] = hide_laser
                enemy_laserX[i] = hide_laser

        # Incrament the player x and y cordinates with the new change from a key press.
        playerX += playerX_change
        playerY += playerY_change

        # Set the bounderies for the player ship.
        if playerX <= 0:
            playerX = 0
        if playerX >= (X - 64):
            playerX = (X - 64)
        if playerY <= 0:
            playerY = 0
        if playerY >= (Y - 64):
            playerY = (Y - 64)

        # Set the bounderies for the shotgun upgrade
        if shotgun_powerY >= Y:
            shotgun_powerY = 0
            shotgun_powerX = random.randint(1, (X - 65))
            shotgun_drop = False
        if shotgun_powerX >= 600:
            shotgun_powerX = random.randint(1, (X - 65))

        # Check to see if the shotgun upgrade should be dropped, if it should be dropped drop it.
        if shotgun_drop:
            shotgun_powerup(shotgun_powerX, shotgun_powerY)
        # Shotgun upgrade movement
            shotgun_powerY += shotgun_power_change

        if score_value >= 25:
            break

        # Draw the player with their last known position update the score and update the display with the new info
        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()
    return score_value, playerX, playerY, enemyY, enemyX
