import sys
import pygame
from time import sleep
# import ship
from bullet import Bullets
from aliens import Alien
def check_events(setti,screen,ship,bullets,stats,aliens):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setti,screen,ship,bullets,)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_KP_ENTER:
            #   mx,my = pygame.mouse.get_pos()
              stats.active_status = True
              empyt_screen(bullets,setti,screen,ship,aliens)
              pygame.mouse.set_visible(False)
        elif event.type == pygame.K_a:
                    stats.active_status = False



def update_screen(setti,stats,screen, ship,bullets,alien,play,scores):
    screen.fill(setti.bg_color)
    for bullet in bullets.sprites():
           bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    if not stats.active_status:
          play.draw_button()
          play.show_inst()
    scores.show_score()
    pygame.display.flip()  


def check_keydown_event(event,setti,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = True
    elif event.key == pygame.K_LEFT:
                ship.moving_left = True
    elif event.key == pygame.K_SPACE:
               fire_bullet(setti,screen,ship,bullets)

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_bullets(setti,screen,ship,aliens,bullets,stats,scores):
    bullets.update()
    for bullet in bullets.copy():
           if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
          stats.scored += setti.redap
          scores.pre_score()
    if(len(aliens) == 0):
           bullets.empty()
           create_fleet(setti,screen,ship,aliens)

def fire_bullet(setti,screen,ship,bullets):
        new_bullet = Bullets(setti,screen,ship)
        bullets.add(new_bullet)

def create_aliens_rows(setti,screen,aliens,row_number):
        alien = Alien(setti,screen)
        alien_width = alien.rect.width
        available_space_x = setti.screen_width - 2*alien_width
        # print(available_space_x,int(alien_width))
        number_aliens_x = 0
        number_aliens_x = int(available_space_x / (2*alien_width))
        # print(number_aliens_x)
        for alien_number in range(number_aliens_x ):
              alien = Alien(setti,screen)
              alien.x = alien_width + 2*alien_width*alien_number
              alien.rect.x = alien.x
              alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
              aliens.add(alien)

def create_fleet(setti,screen,ship,aliens):
       alien = Alien(setti,screen)
       available_space_y = (setti.screen_height - (3*alien.rect.height)-ship.rect.height)
       number_rows = int(available_space_y / (2*alien.rect.height))

       for row_number in range(number_rows):
              create_aliens_rows(setti,screen,aliens,row_number)
              
def check_fleet_edges(setti,aliens,stats,ship,bullets,screen):
       for alien in aliens.sprites():
              if alien.check_edges():
                change_fleet_direction(setti,aliens)
                break
              
def check_fleet_bottom(setti,aliens,stats,ship,bullets,screen):
       for alien in aliens.sprites():
        if alien.check_bottom(screen):
              reset_game(stats,aliens,ship,bullets,screen,setti) 
              break   
        
              
              
def change_fleet_direction(setti,aliens,):
        for alienn in aliens.sprites():
            alienn.rect.y += setti.alien_drop_speed 
        setti.fleet_direction *= -1

def reset_game(stats,aliens,ship,bullets,screen,setti):       
    stats.ships_left -= 1
    if(stats.ships_left > 0):
        empyt_screen(bullets,setti,screen,ship,aliens)
    else:
          stats.active_status = False
          pygame.mouse.set_visible(True)



def update_aliens(setti,aliens,ship,bullets,stats,screen):
        check_fleet_edges(setti,aliens,stats,ship,bullets,screen) 
        check_fleet_bottom(setti,aliens,stats,ship,bullets,screen)  
        aliens.update()         
        if pygame.sprite.spritecollideany(ship,aliens):
          reset_game(stats,aliens,ship,bullets,screen,setti)  

def empyt_screen(bullets,setti,screen,ship,aliens):
        aliens.empty()
    # ship.empty()
        bullets.empty()
    
        create_fleet(setti,screen,ship,aliens)
        ship.center_ship()

        sleep(0.5)

