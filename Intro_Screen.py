from Report_Screen import *
from cut_screen_first_wave import *
from cut_screen_boss_approch import *
from boss_fight import *
pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2 hour tutorial: Space Invaders")
icon = pygame.image.load('Art/001-alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Art/space.png')

# back ground sound
# We only need the bg music to play in this file because this file calls all other files.
mixer.music.load("SFX/bgmusic.wav")
mixer.music.play(-1)

X, Y = pygame.display.get_surface().get_size()
print("Canvas size: ", X, Y)
print("intro screen")

# player image
playerIMG = pygame.image.load('Art/002-space-shuttle.png')

title_font = pygame.font.Font('freesansbold.ttf', 100)
title = title_font.render("Welcome to", True, (255, 255, 255))

title_font2 = pygame.font.Font('freesansbold.ttf', 100)
title2 = title_font2.render("space invaders", True, (255, 255, 255))

command_font = pygame.font.Font('freesansbold.ttf', 50)
command = command_font.render("press enter to play", True, (255, 255, 255))


def intro_screen():
    run = True
    while run:
        win.blit(background, (0, 0))
        win.blit(playerIMG, ((X / 2 - 32), (Y * 4) / 5))
        win.blit(title, ((X/6), (Y - Y)))
        win.blit(title2, ((X/18), ((Y - Y) + 100)))
        win.blit(command, ((X/4), (Y/3)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score_value, playerX, playerY, enemyY, enemyX = game_main()
                    # print(game_score)
                    if score_value >= 25:
                        cut_sceen(playerX, playerY, enemyY, enemyX)
                        cut_sceen_boss()
                        score_value = boss_fight(score_value)
                    report_screen(score_value)

        pygame.display.update()
    return


intro_screen()
