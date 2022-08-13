import pygame
from settings import *
from button import MenuButton
from level import Level

class MainMenu:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE)
        self.btn_width = 200
        self.btn_height = 50
        self.mid_x = WIDTH//2
        self.mid_y = HEIGHT//2
        self.offset_x = self.btn_width//2
        self.offset_y = self.btn_height//2

        self.start_button = MenuButton("START", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y - 100 ), \
            (self.mid_x, (self.mid_y - 100 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.options_button = MenuButton("OPTIONS", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y, ), \
            (self.mid_x, (self.mid_y + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.about_button = MenuButton("ABOUT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 100 ), \
            (self.mid_x, (self.mid_y + 100 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.quit_button = MenuButton("QUIT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 200 ), \
            (self.mid_x, ((self.mid_y) + 200 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )

        self.start = False
        self.level = Level()


    def draw(self):
        self.start_button.update()
        self.options_button.update()
        self.about_button.update()
        self.quit_button.update()

        ### DRAW TITLE SCREEN
        title_surf = pygame.font.Font(MENU_FONT, 80).render("OUT WEST", False, 'black')
        title_rect = title_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 300 + self.offset_y)))
        subtitle_surf = pygame.font.Font(MENU_FONT, 25).render("A tale of BETRAYAL and REDEMPTION in the Old Desert.", False, 'black')        
        subtitle_rect = subtitle_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 200 + self.offset_y)))

        self.display_surface.blit(title_surf, title_rect)
        self.display_surface.blit(subtitle_surf, subtitle_rect)

    def start_game(self):
        pass

    # def update(self):
    #     pass

    def run(self):
        self.draw()
        if self.start == True:
            self.start_game()
            self.level.run_level()


    def game_loop():
        pass