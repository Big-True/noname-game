import pygame

import blocks
import chunks

pygame.init()

logo = pygame.image.load(r'./res/noname-game.ico')
font = pygame.font.Font("./FZMW.TTF", 32)
background = pygame.image.load(r'./res/background.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('noname game')
clock = pygame.time.Clock()
screensize = [800, 600]
screen = pygame.display.set_mode(screensize)
player_pos = [0, 0]
size = 32
speed = 0.1
touch_len = 5.01
block_imgs = [pygame.transform.scale(
    i.res, (size, size)) for i in blocks.block_res]
cover_imgs = [pygame.transform.scale(
    i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.cover_res]
cover_scale = [[i.width, i.height] if i != None else [None, None]
               for i in blocks.cover_res]
player_img = pygame.transform.scale(
    pygame.image.load(r'./res/player.png'), (size, size))
map = chunks.chunk_store('flat')
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
        pos = font.render("(%.2f,%.2f)" %
                          (player_pos[0], player_pos[1]), True, (0, 0, 0))
        for i in range(int(player_pos[0]-screensize[0]/2/size)-1, int(player_pos[0]+screensize[0]/2/size)+1):
            for j in range(int(player_pos[1]-screensize[1]/2/size)-1, int(player_pos[1]+screensize[1]/2/size)+1):
                screen.blit(block_imgs[map.get_block(i, j)], ((i-player_pos[0])*size +
                                                              screensize[0]/2, screensize[1]-((j-player_pos[1]+1)*size+screensize[1]/2)))
        for i in range(int(player_pos[0]-screensize[0]/2/size)-5, int(player_pos[0]+screensize[0]/2/size)+5):
            for j in range(int(player_pos[1]+screensize[1]/2/size)+5, int(player_pos[1]-screensize[1]/2/size)-5, -1):
                if map.get_cover(i, j) != 0:
                    screen.blit(cover_imgs[map.get_cover(i, j)], ((i-player_pos[0]+cover_scale[map.get_cover(i, j)][0]-1)*size +
                                                                  screensize[0]/2, screensize[1]-((j-player_pos[1]+cover_scale[map.get_cover(i, j)][1])*size+screensize[1]/2)))
        screen.blit(
            player_img, ((screensize[0]-size)/2, (screensize[1]-size)/2))
        screen.blit(pos, (0, 0))
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            player_pos[1] += speed
        if key_pressed[pygame.K_a]:
            player_pos[0] -= speed
        if key_pressed[pygame.K_s]:
            player_pos[1] -= speed
        if key_pressed[pygame.K_d]:
            player_pos[0] += speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pow(x-screensize[0]/2, 2)+pow(y-screensize[1]/2, 2) < pow(touch_len*size, 2):
                    t1 = (x-screensize[0]/2)/size+player_pos[0]
                    t2 = (screensize[1]/2-y)/size+player_pos[1]
                    if map.get_cover(int(t1-t1 % 1), int(t2-t2 % 1)) == 0:
                        map.set_block(int(t1-t1 % 1), int(t2-t2 % 1), 0)
                    else:
                        map.set_cover(int(t1-t1 % 1), int(t2-t2 % 1), 0)
    pygame.display.flip()
