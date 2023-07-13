import pygame as pp

class Ship():
    def __init__(self, setti ,screen):
        self.screen = screen
        self.image = pp.image.load('images/ship.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.se = setti
        self.center = float(self.rect.centerx)

    #move
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.rect.centerx += self.se.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.se.ship_speed_factor
        # self.rect.centerx = self.center