import sys, pygame
from settings import *
from mainMenu import MainMenu

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

        # self.sound = pygame.mixer.Sound('./img/Geppetto.mp3')
        # self.sound.play(loops= -1)

    def run(self):
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('beige')
            self.menu.run(keys)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__=='__main__':
    game = Game()
    game.run()