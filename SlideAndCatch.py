# -*- coding: utf-8 -*-
"""
SlideAndCatch

@author: michael.scott
"""
import random
import simpleGE


        
class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Player.png")
        self.sprites = [self]
        self.setSize(50, 50)
        self.position = (320, 400)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Background.png")
        self.player = Player(self)
        self.sprites = [self.player]    
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()


