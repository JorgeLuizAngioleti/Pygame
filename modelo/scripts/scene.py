import pygame
from scripts.obj import Obj
#classe cenas do jogo
class Scene:
    def __init__(self):
        self.display = pygame.display.get_surface()#pega a tela display
        self.all_sprites = pygame.sprite.Group()#grupo de sprites
        self.active = True

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.active = False


    def draw(self):
        self.all_sprites.draw(self.display)#desenhe tudo do grupo

    def update(self):
        self.all_sprites.update()#atualize tudo do grupo