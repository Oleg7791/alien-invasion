import pygame

class Ship:
    """класс для управлением кораблём"""
    def __init__(self,screen):
        """инициализирует корабль и задаёт его начальную позицию"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship1.png')
        new_width = 80
        new_height = 100
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # флаг перемещения
        self.moving_right = False

    def update(self):
        """обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1


    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
