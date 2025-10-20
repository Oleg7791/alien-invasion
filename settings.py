class Settings:
    """ класс для хранения всех настроек игры Alien """

    def __init__(self):
        """ инициализирует настройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)
        # настройки корабля
        self.ship_speed = 0.5