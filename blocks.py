import pygame


class block:
    def __init__(self, name='none', width=1, height=1):
        self.name = name
        self.res = pygame.image.load(r'./res/'+name+r'.png')
        self.width = width
        self.height = height


hole = block('hole')
glass = block('glass')
dirt = block('dirt')
stone = block('stone')
block_res = [hole, glass, dirt, stone]
tree = block('tree', 1, 2)
tree2 = block('tree2', 1, 3)
cover_res = [None, tree, tree2]
