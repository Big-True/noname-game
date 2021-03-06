import pygame

import blocks
import chunks

pygame.init()

logo = pygame.image.load(r'./res/noname-game.ico')
font = pygame.font.Font("./FZMW.TTF", 32)
background = pygame.image.load(r'./res/background.png')
menu_img = pygame.image.load(r'./res/menu.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('noname game')
clock = pygame.time.Clock()
screensize = [800, 600]
screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
player_pos = [0, 0]
size = 32
speed = 0.1
touch_len = 5.01
pack = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
now = 0
choose = pygame.transform.smoothscale(
    pygame.image.load(
        r'./res/item choose.png'), (int(size*1.125), int(size*1.125)))
bar = pygame.image.load(r'./res/item bar.png')
block_imgs = [pygame.transform.smoothscale(
    i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.block_res]
cover_imgs = [pygame.transform.smoothscale(
    i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.cover_res]
cover_scale = [[i.width, i.height] if i != None else [None, None]
               for i in blocks.cover_res]
player_img = pygame.transform.scale(
    pygame.image.load(r'./res/player.png'), (size, size))
map = None
window = 0
running = True
pause = False
pause_img = pygame.image.load(r'./res/pause.png')

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    if window == 0:
        if screensize[0]/16 < screensize[1]/9:
            screen.blit(pygame.transform.scale(
                background, (screensize[0], int(screensize[0]/16*9))), (0, 0))
        else:
            screen.blit(pygame.transform.scale(
                background, (int(screensize[1]/9*16), screensize[1])), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                window = 1
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screensize = event.size
                screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
    elif window == 1:
        screen.blit(menu_img, (int((screensize[0]-800)/2), 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > screensize[0]/2:
                    map = chunks.chunk_store('normal')
                else:
                    map = chunks.chunk_store('flat')
                window = 2
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screensize = event.size
                screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
    elif window == 2:
        pos = font.render('(%.2f,%.2f)' %
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
        screen.blit(bar, (0, 0))
        screen.blit(choose, (8+now*38, 7))
        for i in range(len(pack)):
            if pack[i][0] != 0:
                screen.blit(pygame.transform.smoothscale(
                    blocks.block_res[pack[i][0]].res, (32, 32)), (10+i*38, 9))
                screen.blit(font.render(
                    str(pack[i][1]), True, (0, 0, 0)), (25+i*38, 20))
        screen.blit(pos, (0, screensize[1]-32))
        if pause:
            screen.blit(
                pause_img, (int((screensize[0]-400)/2), int((screensize[1]-400)/2)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.VIDEORESIZE:
                    screensize = event.size
                    screen = pygame.display.set_mode(screensize)
            if sum(pygame.key.get_pressed())+sum(pygame.mouse.get_pressed()) != 0 and pygame.key.get_pressed()[pygame.K_ESCAPE] == 0:
                pause = False
        else:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w]:
                player_pos[1] += speed
            if key_pressed[pygame.K_a]:
                player_pos[0] -= speed
            if key_pressed[pygame.K_s]:
                player_pos[1] -= speed
            if key_pressed[pygame.K_d]:
                player_pos[0] += speed
            if key_pressed[pygame.K_ESCAPE]:
                pause = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_MINUS:
                        size = int(size/2) if size >= 8 else 4
                        block_imgs = [pygame.transform.smoothscale(
                            i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.block_res]
                        cover_imgs = [pygame.transform.smoothscale(
                            i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.cover_res]
                        player_img = pygame.transform.scale(
                            pygame.image.load(r'./res/player.png'), (size, size))
                    if event.key == pygame.K_EQUALS:
                        size = size*2 if size < 128 else 128
                        block_imgs = [pygame.transform.smoothscale(
                            i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.block_res]
                        cover_imgs = [pygame.transform.smoothscale(
                            i.res, (size*i.width, size*i.height)) if i != None else None for i in blocks.cover_res]
                        player_img = pygame.transform.scale(
                            pygame.image.load(r'./res/player.png'), (size, size))
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.VIDEORESIZE:
                    screensize = event.size
                    screen = pygame.display.set_mode(
                        screensize, pygame.RESIZABLE)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    t1 = (x-screensize[0]/2)/size+player_pos[0]
                    t2 = (screensize[1]/2-y)/size+player_pos[1]
                    t1 = int(t1-t1 % 1)
                    t2 = int(t2-t2 % 1)
                    if pow(x-screensize[0]/2, 2)+pow(y-screensize[1]/2, 2) < pow(touch_len*size, 2):
                        if event.button == 1:
                            itid = map.get_cover(t1, t2)
                            if itid == 0:
                                itid = map.get_block(t1, t2)
                                map.set_block(t1, t2, 0)
                            else:
                                map.set_cover(t1, t2, 0)
                            if itid != 0:
                                putted = False
                                for i in range(len(pack)):
                                    if pack[i][0] == itid and not putted:
                                        pack[i][1] += 1
                                        putted = True
                                for i in range(len(pack)):
                                    if pack[i][0] == 0 and not putted:
                                        pack[i] = [itid, 1]
                                        putted = True
                        elif event.button == 3:
                            if pack[now][0] != 0:
                                if map.get_block(t1, t2) == 0:
                                    map.set_block(t1, t2, pack[now][0])
                                    pack[now][1] -= 1
                                    if pack[now][1] == 0:
                                        pack[now][0] = 0
                    if event.button == 4:
                        now = (now-1) % 5
                    if event.button == 5:
                        now = (now+1) % 5
    pygame.display.flip()
