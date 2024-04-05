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
        self.dy = random.randint(5, 20)
        
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
        self.text = "Time: 10"
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.player = Player(self)
        
        self.bgm = simpleGE.Sound("SquirrelMusic.wav")
        self.bgm.play()
        self.pickUp = simpleGE.Sound("AcornGrab.wav")
        
        self.lblScore = lblScore() 
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lblTimer = lblTimer()
        self.prevScore = 0
        
        self.pouch = []
        for i in range(10):
            self.pouch.append(Coin(self))
            
        self.sprites = [self.player, self.pouch, self.lblTimer, self.lblScore]
        
    def process(self):
        for Coin in self.pouch:
            if self.player.collidesWith(Coin):
                Coin.reset()
                self.lblScore.addScore(1)
                self.pickUp.play()
        
        self.lblTimer.text = f"Time: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() <=0:
            self.prevScore = self.lblScore.score
            self.stop()
            print(self.prevScore)
            
            
class startScreen(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("Background.png")
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "As a squirrel, you live to collect Acorns.",
            "Move with the Left and Right arrow keys!",
            "Catch as many Acorns as you can within 10 seconds!",
            "",
            "Use the Up arrow to start!",
            "Or use the down arrow to quit."]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (550, 300)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 420)
        self.btnPlay.text = "Play"
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 420)
        self.btnQuit.text = "Quit"
        
        self.lblPScore = simpleGE.Label()
        self.lblPScore.center = (320, 50)
        self.lblPScore.size = (200, 30)
        self.lblPScore.bgColor = "white"
        self.lblPScore.fgColor = "black"
        self.lblPScore.text = f"previous score: {score} "
        
        self.sprites = [ self.instructions, self.btnPlay, self.btnQuit, self.lblPScore]
             
    def process(self):
        if self.btnQuit.clicked or self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked or self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
            
        
def main():
    keepGoing = True
    score = 1337
    while keepGoing:
        startMenu = startScreen(score)
        startMenu.start()
        if startMenu.response == "Play":
            game = Game()
            game.start()
            score = game.prevScore
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()


