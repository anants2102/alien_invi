import pygame
class Setting():
    def __init__(self):
        #screen setting 
        self.se = pygame.display.get_desktop_sizes()
        self.screen_width = int(1500)
        self.screen_height = int(780)
        self.bg_color = (20,20,20)

        #ship setting
        self.ship_speed_factor = 15

        #bullet setting
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = 230,230,230

        #alien settings
        self.alien_speed_factor = 20
        self.alien_drop_speed = 1
        self.fleet_direction = 10
        