import pygame
from settings import *

class Tile(pygame.sprite.Group):
    def __init__(self, pos, groups, surface=pygame.Surface((TILESIZE, TILESIZE)) ):
        super().__init__(groups)
        self.surface = surface
        self.image = self.surface
        self.rect = self.image.get_rect( topleft=pos )
        self.hitbox = self.rect.inflate(-15, -30)
        # self.rect.y += 20