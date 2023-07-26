import sys
import pygame
from time import sleep
# import ship
from bullet import Bullets,mass_Bullets
from aliens import Alien
def check_events(setti,screen,ship,bullets,stats,aliens,scores,mass_bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setti,screen,ship,bullets,mass_bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type ==pygame.MOUSEBUTTONDOWN or event.type ==  pygame.K_a:
            #   mx,my = pygame.mouse.get_pos()
            if not stats.active_status :
              stats.active_status = True            
              empyt_screen(bullets,setti,screen,ship,aliens,mass_bullets)
              pygame.mouse.set_visible(False)
              scores.pre_ship()
        elif event.type == pygame.K_q:
                 sys.exit()   



def update_screen(setti,stats,screen, ship,bullets,alien,play,scores,mass_bullets):
    screen.fill(setti.bg_color)
    for bullet in bullets.sprites():
           bullet.draw_bullet()
    for bullets in mass_bullets.sprites():
          bullets.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    if not stats.active_status:
          play.draw_button()
        #   play.show_inst(inst)
    scores.show_score()
    pygame.display.flip()  


def check_keydown_event(event,setti,screen,ship,bullets,mass_bullets):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = True
    elif event.key == pygame.K_LEFT:
                ship.moving_left = True
    elif event.key == pygame.K_SPACE:
               fire_bullet(setti,screen,ship,bullets)
    elif event.key == pygame.K_i:
           fire_mass_bullets(setti,screen,ship,mass_bullets)

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_bullets(setti,screen,ship,aliens,bullets,stats,scores,mass_bullets):
    bullets.update()
    mass_bullets.update()
    for bullet in bullets.copy():
           if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
    for bullet in mass_bullets.copy():
           if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    collisionss = pygame.sprite.groupcollide(mass_bullets,aliens,True,True)
    if collisions:
          for aliens in collisions.values():
            stats.scored += setti.redap*len(aliens)
            scores.pre_score()
    elif collisionss:
          for aliens in collisions.values():
                stats.scored += setti.redap*len(aliens)
                scores.pre_score()
    if(len(aliens) == 0):
           bullets.empty()
           create_fleet(setti,screen,ship,aliens)

def fire_bullet(setti,screen,ship,bullets):
        new_bullet = Bullets(setti,screen,ship)
        bullets.add(new_bullet)
def fire_mass_bullets(setti,screen,ship,bullets):
        new_bullet = mass_Bullets(setti,screen,ship)
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
              
def check_fleet_edges(setti,aliens,stats,ship,bullets,screen,mass_bullets):
       for alien in aliens.sprites():
              if alien.check_edges():
                change_fleet_direction(setti,aliens)
                break
              
def check_fleet_bottom(setti,aliens,stats,ship,bullets,screen,scores,mass_bullets):
       for alien in aliens.sprites():
        if alien.check_bottom(screen):
              reset_game(stats,aliens,ship,bullets,screen,setti,scores,mass_bullets) 
              break   
        
              
              
def change_fleet_direction(setti,aliens,):
        for alienn in aliens.sprites():
            alienn.rect.y += setti.alien_drop_speed 
        setti.fleet_direction *= -1

def reset_game(stats,aliens,ship,bullets,screen,setti,scores,mass_bullets):       
    stats.ships_left -= 1
    if(stats.ships_left > 0):
        scores.pre_ship()
        empyt_screen(bullets,setti,screen,ship,aliens,mass_bullets)    
    else:
          stats.scored = 0
          stats.active_status = False
          stats.reset_stats()
          pygame.mouse.set_visible(True)



def update_aliens(setti,aliens,ship,bullets,stats,screen,scores,mass_bullets):
        check_fleet_edges(setti,aliens,stats,ship,bullets,screen,mass_bullets) 
        check_fleet_bottom(setti,aliens,stats,ship,bullets,screen,scores,mass_bullets)  
        aliens.update()         
        if pygame.sprite.spritecollideany(ship,aliens):
          reset_game(stats,aliens,ship,bullets,screen,setti,scores,mass_bullets)  

def empyt_screen(bullets,setti,screen,ship,aliens,mass_bullets):
        aliens.empty()
    # ship.empty()
        bullets.empty()
        mass_bullets.empty()
        sleep(2)
        create_fleet(setti,screen,ship,aliens)
        ship.center_ship()


