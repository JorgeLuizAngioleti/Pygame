import pygame, sys
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.game import Game
from scripts.gameover import GameOver
from scripts.settings import *

class StartGame:
	def __init__(self):
		pygame.init()#inicializa os videos
		pygame.mixer.init()#inicializa os sons
		pygame.font.init()#iniicializa as fontes
		self.display = pygame.display.set_mode((LARGURA,ALTURA))
		self.scene = 'menu'
		self.current_scene = Menu()#instanciamos a classe scene
	def run(self):

		while True:
			if self.scene == 'menu' and self.current_scene.active == False:
				self.scene = 'game'
				self.current_scene = Game()
			elif self.scene == 'game' and self.current_scene.active == False:
				self.scene = 'gameover'
				self.current_scene = GameOver()
			elif self.scene == 'gameover' and self.current_scene.active == False:
				self.scene = 'menu'
				self.current_scene = Menu()


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()#encerra o loop do pygame
					sys.exit()#encerra o terminal do pytohn
				self.current_scene.events(event)#chamando  o metodo da classe cena
			self.display.fill("black")
			self.current_scene.draw()#chama evento de desenho
			self.current_scene.update()#chama a atualização do jogo
			pygame.display.flip()