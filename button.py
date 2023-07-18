import pygame.font

class Button():

    def __init__(self,setti,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width,self.height = 700,50
        self.button_color = (230,230,230)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
        self.inst = "press mouse key to start"

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    def show_inst(self):
        self.inst_image = self.font.render(self.inst,True,(230,230,230),(0,0,0))
        self.inst_image_rect = self.inst_image.get_rect()
        self.inst_image_rect.center = self.rect.center