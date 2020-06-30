from GameMain import *

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2 hour tutorial: Space Invaders")
icon = pygame.image.load('Art/001-alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Art/space.png')

X, Y = pygame.display.get_surface().get_size()
print("Canvas size: ", X, Y)
print("report screen")

# player image
playerIMG = pygame.image.load('Art/002-space-shuttle.png')

title_font = pygame.font.Font('freesansbold.ttf', 100)
title = title_font.render("You Scored:", True, (255, 255, 255))

command_font = pygame.font.Font('freesansbold.ttf', 50)
command = command_font.render("press enter to exit", True, (255, 255, 255))

score_font = pygame.font.Font('freesansbold.ttf', 50)


def report_screen(game_score):
    score = score_font.render(str(game_score), True, (255, 255, 255))
    congrats = score_font.render("Congrats you beat the game", True, (255, 255, 255))
    congrats2 = score_font.render("your score was " + str(game_score), True, (255, 255, 255))

    run = True
    while run:
        win.blit(background, (0, 0))
        win.blit(playerIMG, ((X / 2 - 32), (Y * 4) / 5))

        if game_score < 125:
            win.blit(title, ((X / 6), 0))
            win.blit(score, (((X / 2) - 30), 100))
            win.blit(command, (((X / 2) - 220), 160))

        if game_score >= 125:
            win.blit(title, ((X / 6), 0))
            win.blit(congrats, (((X / 2) - 330),  100))
            win.blit(congrats2, (((X / 2) - 210), 160))
            win.blit(command, ((X / 2) - 210, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False

        pygame.display.update()
    return


# Use for testing
# report_screen(200)
