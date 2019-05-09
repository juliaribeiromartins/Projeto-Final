# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:15:50 2019

@author: julia
"""

import pygame
import os
import random


WIDTH=500 #largura
HEIGHT=500 #altura
FPS=30 #frames per second





pygame.init() #para começar
pygame.mixer.init() #som
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("nosso jogo")
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p3_jump.png')).convert()

#vou definir as variáveis que contém as cores
AZUL=(0,180,255)
ROSA=(255,0,150) #vermelho,verde,azul
BLACK=(0,0,0)
WHITE=(255,255,255)


class Player(pygame.sprite.Sprite):
    def __init__(self): #a funçao que define qual codigo sera executado sempre que um novo objeto desse tipo for criado
        pygame.sprite.Sprite.__init__(self)#inicializador de classe
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect() #rect é retangulo
        self.rect.y = random.randrange(0,HEIGHT)
        self.rect.x = random.randrange(0,2)
        self.speedx =random.randrange(2,15)
        self.speedy =random.randrange(0,1)
        
    def update(self):
       self.rect.y+= self.speedy
       self.rect.x+= self.speedx
       if self.rect.top > HEIGHT + 10 or self.rect.left < -50 or self.rect.right > WIDTH + 50:
           self.rect.y = random.randrange(0,HEIGHT)
           self.rect.x = random.randrange(0,2)
           
           velocidade_min_x=-5
           velocidade_max_x=5
           velocidade_max_x=velocidade_max_x - velocidade_max_x*self.rect.x/WIDTH
           velocidade_min_x=velocidade_min_x - velocidade_min_x*(1 - self.rect.x/WIDTH)
           
           self.speedx =random.uniform(velocidade_min_x, velocidade_max_x )
           self.speedy =random.randrange(0,1)
           
       


p=pygame.sprite.Group()      

for i in range(0,8):
    player= Player()
    all_sprites.add(player)
    p.add(player)     





#game loop
running=True 
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    all_sprites.update() #to chamando o grupo para desenhar na tela        
    screen.fill(AZUL) #cor da tela
    all_sprites.draw(screen) #to chamando a função para o grupo inteiro ser desenhado
    pygame.display.flip()#atualizar depois que vc "desenha"
    #a partir de agora todos os grupos serao desenhados na tela e atualizados
pygame.quit()
quit()
    

          
         #self.speedx =random.uniform(velocidade_min_x, velocidade_max_x )
         #self.speedy =random.randrange(5,9)  
         
   # if self.rect.top > HEIGHT + 10 or self.rect.left < -50 or self.rect.right > WIDTH + 50:
           
           #self.rect.y = random.randrange(0,HEIGHT)
           #self.rect.x = random.randrange(0,2)
           
           #velocidade_min_x=-5
           #velocidade_max_x=5
           #velocidade_max_x=velocidade_max_x - velocidade_max_x*self.rect.x/WIDTH
           #velocidade_min_x=velocidade_min_x - velocidade_min_x*(1 - self.rect.x/WIDTH)
           
           #self.speedx =random.uniform(velocidade_min_x, velocidade_max_x )
           #self.speedy =random.randrange(5,9)
           
    
    
    
#if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20: