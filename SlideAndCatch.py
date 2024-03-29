# -*- coding: utf-8 -*-
"""
SlideAndCatch

@author: michael.scott
"""
import random, simpleGE, pygame
  
score = 0
  
class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Player.png")
        self.sprites = [self]
        self.setSize(50, 50)
        self.position = (320, 400)
        self.movespeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.movespeed 
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.movespeed

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("coin.png")
        self.sprites = [self]
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = 10
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

    def collide(self):
        if self.collidesWith(Player(self)):
            self.reset()

        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.player = Player(self)
        self.coin = Coin(self)
        self.sprites = [self.player, self.coin]

    def process(self):
        if self.coin.collidesWith(self.player):
            self.coin.reset()
            score += 1
            print(score)
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()


