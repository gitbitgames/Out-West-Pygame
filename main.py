import sys, pygame
from settings import *
from mainMenu import MainMenu
from game import GameLoop

class Game:
    def __init__(self):
        ### Pygame initialization
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        ### Change to fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display_surface = pygame.display.get_surface()
        self.menu = MainMenu()
        pygame.display.set_caption('Out West')
        self.clock = pygame.time.Clock()
        self.start = False
        self.game = GameLoop()
        # self.sound = pygame.mixer.Sound('./img/Geppetto.mp3')
        # self.sound.play(loops= -1)

    def check_exit(self, keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            keys = pygame.key.get_pressed()
            self.check_exit(keys)
            self.screen.fill('beige')
            if self.menu.start:
                # self.menu.fade_to_black(self.screen)
                while True:
                    keys = pygame.key.get_pressed()
                    self.screen.fill('beige')
                    self.check_exit(keys)
                    self.game.run()
                    pygame.display.update()
                    self.clock.tick(FPS)
            self.menu.run(keys)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__=='__main__':
    game = Game()
    game.run()