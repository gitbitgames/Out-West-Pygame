import pygame
from settings import *

class MenuButton:
    def __init__(self, text, width, height, pos, text_pos, btn_color, border_color, surface):
        self.display_surface = surface
        self.rect = pygame.Rect(pos, (width, height))
        self.font = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE)
        self.font_color = pygame.Color(245, 245, 220)
        self.color = btn_color
        self.border = border_color
        self.pos = pos
        self.offset_x = width//2
        self.offset_y = height//2
        self.text = text
        self.text_pos = text_pos
        self.click_timer = 0
        self.current_time = 0
        self.clicked = False

    def draw(self):
        pygame.draw.rect(self.display_surface, self.border, self.rect.inflate(10, 10), border_radius=12)
        pygame.draw.rect(self.display_surface, self.color, self.rect, border_radius=12)
        text_surf = self.font.render(self.text, False, self.font_color)
        text_rect = text_surf.get_rect(center=self.text_pos)
        self.display_surface.blit(text_surf, text_rect)

    def update(self):
        self.current_time = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0]:
            self.check_click()
        if self.clicked == True and self.current_time - self.click_time >= 60:
            self.clicked = False
            self.color = MENU_BUTTON_COLOR
        self.draw()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.text != 'START':
                self.color = 'white'
            self.click_time = pygame.time.get_ticks()
            self.clicked = True