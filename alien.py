import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ класс представляющий пришельцев"""

    def __init__(self,ai_game):
        """инициализирует пришельца и задаёт его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # загрузка изображение пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien2.xcf').convert_alpha()

        new_width = 60
        new_height = 50
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
        self.rect = self.image.get_rect()

        # каждый пришелец появляется в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """ перемещает пришельца влево или вправо"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True