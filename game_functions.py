import sys
import pygame
# import ship
from bullet import Bullets
from aliens import Alien
def check_events(setti,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setti,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(setti,screen, ship,bullets,alien):
    screen.fill(setti.bg_color)
    for bullet in bullets.sprites():
           bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
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

def update_bullets(aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
           if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

def fire_bullet(setti,screen,ship,bullets):
        new_bullet = Bullets(setti,screen,ship)
        bullets.add(new_bullet)

def create_aliens_rows(setti,screen,aliens,row_number):
        alien = Alien(setti,screen)
        alien_width= alien.rect.width
        available_space_x = setti.screen_width - 2*alien_width
        number_aliens_x = int(available_space_x / 2*alien_width)-3
        for alien_number in range(number_aliens_x):
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
              
def check_fleet_edges(setti,aliens):
       for alien in aliens.sprites():
              if alien.check_edges():
                change_fleet_direction(setti,aliens)   
                break
              
def change_fleet_direction(setti,aliens):
        for alienn in aliens.sprites():
            alienn.rect.y += setti.alien_drop_speed
        setti.fleet_direction *= -1

def update_aliens(setti,aliens):
        check_fleet_edges(setti,aliens)   
        aliens.update()                 
       

