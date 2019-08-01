import pygame
pygame.init()
logo = pygame.image.load(r'./res/noname-game.ico')
background = pygame.image.load(r'./res/background.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('noname game')
clock = pygame.time.Clock()
screensize = [800, 600]
screen = pygame.display.set_mode(screensize)
player_pos = [0, 0]
map = []
window = 0
running = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    if window == 0:
        if screensize[0]/1920 < screensize[1]/1080:
            background = pygame.transform.scale(
                background, (screensize[0], int(screensize[0]/16*9)))
        else:
            background = pygame.transform.scale(
                background, (int(screensize[1]/9*16), screensize[1]))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                window = 1
            if event.type == pygame.QUIT:
                running = False
    elif window == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
