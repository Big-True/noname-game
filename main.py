import pygame
pygame.init()
logo=pygame.image.load(r'./res/noname-game.ico')
pygame.display.set_icon(logo)
pygame.display.set_caption('noname game')
clock = pygame.time.Clock()
screensize=[800,600]
screen=pygame.display.set_mode(screensize)
player_pos=[0,0]
map=[]
window=0
running=True

while running:
    clock.tick(60)
    if window==0:
        pass
    elif window==1:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.flip()