import sys 
import pygame
from ship import Ship
from settings import Setting
from pygame.sprite import Group
import game_functions as gf
from aliens import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
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
    play = Button(setti,screen,"Play")
    scores = Scoreboard(setti,screen,stats)
    gf.create_fleet(setti,screen,ship,aliens)
    
    while True:
     gf.update_screen(setti,stats,screen,ship,bullets,aliens,play,scores)
     gf.check_events(setti,screen,ship,bullets,stats,aliens,scores)
     if stats.active_status:
       ship.update()
       gf.update_bullets(setti,screen,ship,aliens,bullets,stats,scores)
       gf.update_aliens(setti,aliens,ship,bullets,stats,screen,scores)
    #  else:
    #    print("not active")
    #    break

run_game() 
