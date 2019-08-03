import pygame


class block:
    def __init__(self, name='none'):
        self.name = name
        self.res = pygame.image.load(r'./res/'+name+r'.png')


glass = block('glass')
dirt = block('dirt')
stone = block('stone')
block_res = [glass, dirt, stone]
