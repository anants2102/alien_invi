import sys 
import pygame
from ship import Ship
from settings import Setting
from pygame.sprite import Group
import game_functions as gf
from aliens import Alien
from game_stats import GameStats
def run_game():
    pygame.init()
    setti = Setting()
    # print(setti.screen_width + 12)  
    screen = pygame.display.set_mode((setti.screen_width,setti.screen_height))
    pygame.display.set_caption("Alien Invasion") 
    ship = Ship(setti,screen)
    # alien = Alien(setti,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(setti)
    gf.create_fleet(setti,screen,ship,aliens)
    while True:
     if stats.active_status:
       gf.check_events(setti,screen,ship,bullets)

       ship.update()
       gf.update_bullets(setti,screen,ship,aliens,bullets)
       gf.update_aliens(setti,aliens,ship,bullets,stats,screen)
       gf.update_screen(setti,screen,ship,bullets,aliens)  
     else:
       break

run_game() 
