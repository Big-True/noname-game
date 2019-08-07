import pygame


class block:
    def __init__(self, name='none', width=1, height=1):
        self.name = name
        self.res = pygame.image.load(r'./res/'+name+r'.png')
        self.width = width
        self.height = height


hole = block('hole')
grass = block('grass')
dirt = block('dirt')
stone = block('stone')
wood = block('wood')
block_res = [hole, grass, dirt, stone, wood]
tree = block('tree', 1, 2)
cover_res = [None, None, None, None, tree]
items = [None, grass, dirt, stone, tree]
