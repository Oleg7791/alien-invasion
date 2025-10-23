import pygame

class Ship:
    """класс для управлением кораблём"""
    def __init__(self,ai_game):
        """инициализирует корабль и задаёт его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship1.png')
        new_width = 80
        new_height = 100
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновляет позицию корабля с учетом флага."""
        # обновляется атрибут х, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # обновление атрибута rect на основании self.x
        self.rect.x = self.x


    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
