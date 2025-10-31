class Settings:
    """ класс для хранения всех настроек игры Alien """

    def __init__(self):
        """ инициализирует статические настройки игры"""

        # настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 220)
        # настройки корабля
        #self.ship_speed = 1
        self.ship_limit = 3

        # параметры снаряда
        #self.bullet_speed = 3
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = (250,128,0)
        self.bullet_allowed = 3

        # настройки пришельцев
        #self.alien_speed = .3
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1

        # темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """ инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed = 1
        self.bullet_speed = 3.0
        self.alien_speed = 0.3

        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        """ увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale