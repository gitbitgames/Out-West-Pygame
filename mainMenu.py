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
            (self.mid_x, (self.mid_y - 100 + self.offset_y)), pygame.Color(191, 128, 64), MENU_BUTTON_BORDER, self.display_surface )
        self.options_button = MenuButton("OPTIONS", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y, ), \
            (self.mid_x, (self.mid_y + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.about_button = MenuButton("ABOUT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 100 ), \
            (self.mid_x, (self.mid_y + 100 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.quit_button = MenuButton("QUIT", self.btn_width, self.btn_height, ( self.mid_x - self.offset_x, self.mid_y + 200 ), \
            (self.mid_x, ((self.mid_y) + 200 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.back_button = MenuButton("BACK TO MAIN MENU", self.btn_width*1.5, self.btn_height, ( self.mid_x - ((self.btn_width*1.5)//2), self.mid_y + 150 ), \
            (self.mid_x, ((self.mid_y) + 150 + self.offset_y)), MENU_BUTTON_COLOR, MENU_BUTTON_BORDER, self.display_surface )
        self.buttons = (self.start_button, self.options_button, self.about_button, self.quit_button)

        for idx, text_line in enumerate(ABOUT):
            about_surf = pygame.font.Font(MENU_FONT, MENU_FONT_SIZE).render(text_line, False, 'black')
            about_rect = about_surf.get_rect(center=(self.mid_x, (self.mid_y - 100 + (idx*25) + self.offset_y)))
            self.about_text.append([about_surf, about_rect])

        self.imageSrc1 = pygame.transform.scale(pygame.image.load("./img/Player/movement/down_idle/01.png").convert_alpha(), (500, 500))
        self.imageSrc2 = pygame.transform.scale(pygame.image.load("./img/Player/tree.png").convert_alpha(), (600, 600))
        self.imageSrc3 = pygame.transform.scale(pygame.image.load("./img/Player/bush.png").convert_alpha(), (300, 150))
        self.imageSrc4 = pygame.transform.scale(pygame.image.load("./img/Player/plant.png").convert_alpha(), (100, 100))
        self.imageSrc5 = pygame.transform.scale(pygame.image.load("./img/Player/plant2.png").convert_alpha(), (100, 100))
        self.start = False
        self.level = Level()

    def draw(self, keys):
        if not self.about:
            for button in self.buttons:
                button.update()
        else:
            self.about_button.clicked = False
            self.about_button.color = MENU_BUTTON_COLOR
            for line in self.about_text:
                self.display_surface.blit(line[0], line[1])
            self.back_button.update()
            if self.back_button.clicked:
                self.about = False

        ### DRAW TITLE SCREEN
        title_surf = pygame.font.Font(MENU_FONT, 80).render("OUT WEST", False, 'black')
        title_rect = title_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 300 + self.offset_y)))
        subtitle_surf = pygame.font.Font(MENU_FONT, 25).render("A tale of BETRAYAL and REDEMPTION in the Old Desert.", False, 'black')        
        subtitle_rect = subtitle_surf.get_rect(center=(self.mid_x, ((self.mid_y) - 200 + self.offset_y)))

        self.display_surface.blit(title_surf, title_rect)
        self.display_surface.blit(subtitle_surf, subtitle_rect)
        self.display_surface.blit(self.imageSrc1, (100,400))
        self.display_surface.blit(self.imageSrc3, (900,500))
        self.display_surface.blit(self.imageSrc4, (950,630))
        self.display_surface.blit(self.imageSrc5, (820, 600))
        self.display_surface.blit(self.imageSrc2, (860,200))


    def check_clicks(self):
        if self.start_button.clicked == True:
            self.start = True
            # self.start_game()
        if self.quit_button.clicked == True:
            pygame.quit()
            sys.exit()
        if self.about_button.clicked == True:
            self.about = True


    def run(self, keys):
        self.check_clicks()
        self.draw(keys)

    # def fade_to_black(self, window):
    #     r, g, b = (191, 128, 64)
    #     r2, g2, b2 = (245, 245, 220)
    #     fade = pygame.Surface((self.mid_x*2, self.mid_y*2))
    #     fade.fill((0,0,0))
    #     for alpha in range(300):
    #         if r != 0: r -= 1
    #         if g != 0: g -= 1
    #         if b != 0: b -= 1
    #         if r2 != 0: r2 -= 1
    #         if g2 != 0: g2 -= 1
    #         if b2 != 0: b2 -= 1

    #         fade.set_alpha(alpha)
    #         window.fill((255,255,255))
    #         window.blit(fade, (0,0))
    #         for button in self.buttons:
    #             button.color = pygame.Color(r, g, b)
    #             button.border = pygame.Color(r, g, b)
    #             button.font_color = pygame.Color(r2, g2, b2)
    #         self.draw([])
    #         pygame.display.update()