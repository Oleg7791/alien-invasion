import pygame

class Ship2:
    """создадим ещё один класс с кораблем"""

    def __init__(self,screen):
         """инициализируем корабль с начальной позицией"""

         self.screen = screen
         self.screen_rect = screen.get_rect()
         self.player = pygame.image.load('images/ship2.png')
         new_width = 100
         new_height = 200
         self.player = pygame.transform.scale(self.player,(new_width,new_height))
         self.player_rect = self.player.get_rect()
         self.player_rect.bottomright = self.screen_rect.bottomright

    def blet(self):
        self.screen.blit(self.player,self.player_rect)