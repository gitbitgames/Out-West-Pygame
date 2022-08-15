from turtle import down
import pygame, sys
from entity import Entity
from settings import *
from support import *

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites

        self.image = pygame.image.load('./img/player.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.status = 'right_idle'
        self.speed = 5
        self.animations = self.import_player_assets()

    def import_player_assets(self):
        character_path = './img/Player/movement/'
        animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': [],
            'ne': [],
            'ne_idle': [],
            'nw': [],
            'nw_idle': [],
            'se': [],
            'se_idle': [],
            'sw': [],
            'sw_idle': []
        }
        for animation in animations.keys():
            full_path = character_path + animation
            animations[animation] = import_player_folder(full_path)
        return animations

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def animate(self):        
        animation = self.animations[self.status]

        # Loop our frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Round the index and set the image        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_status(self):
        if self.direction.x == 1:
            if self.direction.y == 1:
                self.status = 'se'
            elif self.direction.y == -1:
                self.status = 'ne'
            else:
                self.status = 'right'
        elif self.direction.x == -1:
            if self.direction.y == 1:
                self.status = 'sw'
            elif self.direction.y == -1:
                self.status = 'nw'
            else:
                self.status = 'left'
        elif self.direction.y == 1:
            self.status = 'down'
        elif self.direction.y == -1:
            self.status = 'up'  

        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'

    def update(self):
        self.move(self.speed)
        self.player_input()
        self.get_status()
        self.animate()