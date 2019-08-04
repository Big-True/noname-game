import pygame

import blocks
import chunks

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
speed = 0.1
block_imgs = [pygame.transform.scale(
    i.res, (size, size)) for i in blocks.block_res]
player_img = pygame.transform.scale(
    pygame.image.load(r'./res/player.png'), (size, size))
map = chunks.chunk_store()
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
        for i in range(int(player_pos[0]-screensize[0]/2/size)-1, int(player_pos[0]+screensize[0]/2/size)+1):
            for j in range(int(player_pos[1]-screensize[1]/2/size)-1, int(player_pos[1]+screensize[1]/2/size)+1):
                screen.blit(block_imgs[map.get_block(i, j)], ((i-player_pos[0])*size +
                                                              screensize[0]/2, (j-player_pos[1])*size+screensize[1]/2))
        screen.blit(
            player_img, ((screensize[0]-size)/2, (screensize[1]-size)/2))
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            player_pos[1] -= speed
        if key_pressed[pygame.K_a]:
            player_pos[0] -= speed
        if key_pressed[pygame.K_s]:
            player_pos[1] += speed
        if key_pressed[pygame.K_d]:
            player_pos[0] += speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
