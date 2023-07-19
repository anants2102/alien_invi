import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    def __init__(self,setti,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setti = setti
        self.text_color = (230,230,230)
        self.font = pygame.font.SysFont(None,48)
        self.stats = stats
        self.pre_score()
        self.pre_ship()
    
    def pre_score(self):
        self.score_str = str(self.stats.scored)
        self.score_image = self.font.render(self.score_str,True,self.text_color,self.setti.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)

    def pre_ship(self):
        self.ships = Group()
        for ship_no in range(self.stats.ships_left):
            ship = Ship(self.setti,self.screen)
            ship.rect.x = 10 + ship_no * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)