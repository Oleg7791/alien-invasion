class Settings:
    """ класс для хранения всех настроек игры Alien """

    def __init__(self):
        """ инициализирует настройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 220)
        # настройки корабля
        self.ship_speed = 1.5

        # параметры снаряда
        self.bullet_speed = 1
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3