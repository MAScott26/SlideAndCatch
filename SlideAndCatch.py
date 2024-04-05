# -*- coding: utf-8 -*-
"""
SlideAndCatch

@author: michael.scott
"""
import random, simpleGE, pygame
  

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("squirrel.png")
        self.sprites = [self]
        self.setSize(50, 50)
        self.position = (320, 400)
        self.movespeed = 5
        self.flip = False
    def process(self):
        
        if self.isKeyPressed(pygame.K_LEFT):
            if self.flip == True:
                self.flip = False
                self.image = pygame.transform.flip(self.image, True, False )
            self.x -= self.movespeed 
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.flip == False:
                self.flip = True
                self.image = pygame.transform.flip(self.image, True, False )
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


class lblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (100, 20)
        self.score = 0
        self.text = f"Score: {self.score}"
    
    def addScore(self, scoreChange):
        self.score += scoreChange
        self.text = f"Score: {self.score}"
        
        
class lblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (500, 20)
        self.text = "TIMER"
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.player = Player(self)
        
        self.lblScore = lblScore() 
        self.timerBoard = lblTimer()
        
        self.pouch = []
        for i in range(10):
            self.pouch.append(Coin(self))
            
        self.sprites = [self.player, self.pouch, self.timerBoard, self.lblScore]
        
    def process(self):
        for Coin in self.pouch:
            if self.player.collidesWith(Coin):
                Coin.reset()
                self.lblScore.addScore(1)
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()


