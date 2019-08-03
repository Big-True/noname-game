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
size = 32
speed = 5
block_imgs = [pygame.transform.scale(
    pygame.image.load(r'./res/glass.png'), (size, size)),pygame.transform.scale(
    pygame.image.load(r'./res/player.png'), (size, size))]
player_img = pygame.transform.scale(
    pygame.image.load(r'./res/player.png'), (size, size))
map = []
window = 0
running = True


def newmap():
    global map
    map = [[1 for i in range(100)]for j in range(100)]
    map[0][0]=2


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
                newmap()
                window = 1
            if event.type == pygame.QUIT:
                running = False
    elif window == 1:
        for i in range(int(player_pos[0]-screensize[0]/2/size), int(player_pos[0]+screensize[0]/2/size)+1):
            for j in range(int(player_pos[1]-screensize[1]/2/size), int(player_pos[1]+screensize[1]/2/size)+1):
                if i >= 0 and j >= 0 and i<len(map[0]) and j<len(map):
                    screen.blit(block_imgs[map[j][i]-1], ((i-player_pos[0])*size +
                                                          screensize[0]/2, (j-player_pos[1])*size+screensize[1]/2))
        screen.blit(
            player_img, ((screensize[0]-size)/2, (screensize[1]-size)/2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_pos[1] -= speed
                if event.key == pygame.K_a:
                    player_pos[0] -= speed
                if event.key == pygame.K_s:
                    player_pos[1] += speed
                if event.key == pygame.K_d:
                    player_pos[0] += speed
    pygame.display.flip()
