import sys
import pygame
from ship2 import Ship2

class Screen:
    """создадим класс описывающий экран"""



    def __init__(self):
        """ инициализация экрана"""
        self.color = (30,150,250)
        self.screen_width =   700
        self.screen_height =  800
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.ship = Ship2(self.screen)

    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.color)
            self.ship.blet()
            pygame.display.flip()




if __name__ == '__main__':
    pl = Screen()
    pl.run_screen()