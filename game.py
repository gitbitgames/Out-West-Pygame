import pygame
from settings import *
from support import *
from player import Player
from tile import Tile

class GameLoop:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE)
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player = Player((0,0), [self.visible_sprites], self.obstacle_sprites)
        self.create_map()

    def draw(self, surface):
        pass

    def run(self):
        # self.draw(self.display_surface)
        self.player.player_input()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


    def create_map(self):
        Tile((10, 10), [self.visible_sprites], self.player.image)
        img = pygame.image.load('./img/00.png')

        for row_idx, row in enumerate(MAP):
            for col_idx, col in enumerate(row):
                if col == 'x':
                    x = col_idx * TILESIZE
                    y = row_idx * TILESIZE
                    Tile((x, y), [self.visible_sprites], img)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # create the floor
        self.floor_surf = pygame.transform.scale(pygame.image.load('./img/OldWest.png').convert(), (13500,4500))
        self.floor_rect = self.floor_surf.get_rect(topleft = (-7000,-1600))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

            ### This loop fixes the hitbox issues with overlapping sprites
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    # def npc_update(self, player):
    #     npc_sprites = [ sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'npc' ]
    #     for npc in npc_sprites:
    #         npc.update(player)