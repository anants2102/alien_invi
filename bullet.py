import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self,setti,screen,ship):
        super(Bullets,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,setti.bullet_width,setti.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = setti.bullet_color
        self.speed_factor = setti.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class mass_Bullets(Sprite):
    def __init__(self,setti,screen,ship):
        self.screen = screen
        super(mass_Bullets,self).__init__()
        self.rect = pygame.Rect(0,0,1200,setti.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = setti.bullet_color
        self.speed_factor = setti.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)