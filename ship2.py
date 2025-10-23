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
        self.player_rect.midbottom = self.screen_rect.midbottom
        self.rect = self.player.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update_ship(self):
        if self.moving_right:
            self.rect.x += 1

    def blet(self):
        self.screen.blit(self.player,self.player_rect)