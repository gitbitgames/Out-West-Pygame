import sys, pygame
from settings import *
from button import MenuButton
from level import Level

class MainMenu:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE)
        self.btn_width = 200
        self.btn_height = 50
        self.mid_x = pygame.display.get_window_size()[0] // 2
        self.mid_y = pygame.display.get_window_size()[1] // 2
        self.offset_x = self.btn_width//2
        self.offset_y = self.btn_height//2
        self.about = False
        self.about_text = []


        self.start_button = MenuButton("START", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y - 100 ), \
            (self.mid_x, (self.mid_y - 100 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.options_button = MenuButton("OPTIONS", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y, ), \
            (self.mid_x, (self.mid_y + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.about_button = MenuButton("ABOUT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 100 ), \
            (self.mid_x, (self.mid_y + 100 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.quit_button = MenuButton("QUIT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 200 ), \
            (self.mid_x, ((self.mid_y) + 200 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )


        for idx, text_line in enumerate(ABOUT):
            about_surf = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE).render(text_line, False, 'black')
            about_rect = about_surf.get_rect(center=(self.mid_x, (self.mid_y - 100 + (idx*25) + self.offset_y)))
            self.about_text.append([about_surf, about_rect])

        self.start = False
        self.level = Level()

    def draw(self, keys):
        if not self.about:
            self.start_button.update()
            self.options_button.update()
            self.about_button.update()
            self.quit_button.update()
        else:
            self.about_button.clicked = False
            self.about_button.color = MENU_BUTTON_COLOR
            for line in self.about_text:
                self.display_surface.blit(line[0], line[1])
            if keys[pygame.K_RETURN]:
                self.about = False

        ### DRAW TITLE SCREEN
        title_surf = pygame.font.Font(MENU_FONT, 80).render("OUT WEST", False, 'black')
        title_rect = title_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 300 + self.offset_y)))
        subtitle_surf = pygame.font.Font(MENU_FONT, 25).render("A tale of BETRAYAL and REDEMPTION in the Old Desert.", False, 'black')        
        subtitle_rect = subtitle_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 200 + self.offset_y)))

        self.display_surface.blit(title_surf, title_rect)
        self.display_surface.blit(subtitle_surf, subtitle_rect)

    def start_game(self):
        self.game_loop()

    def check_clicks(self):
        if self.start_button.clicked == True:
            self.start == True
            self.start_game()
        if self.quit_button.clicked == True:
            pygame.quit()
            sys.exit()
        if self.about_button.clicked == True:
            self.about = True


    def run(self, keys):
        self.check_clicks()
        self.draw(keys)        

    def game_loop():
        pass