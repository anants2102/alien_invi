import pygame
class Setting():
    def __init__(self):
        #screen setting 
        self.se = pygame.display.get_desktop_sizes()
        self.screen_width = int(1200)
        self.screen_height = int(780)
        self.bg_color = (20,20,20)

        #ship setting
        self.ship_speed_factor = 1
        self.ship_limit = 3

        #bullet setting
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = 230,230,230

        #alien settings
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        self.fleet_direction = 1
        
        #scoring
        self.redap = 10


    