#!/usr/bin/python

###############################################################################
#                                                                             #
#                           THE HUNGRY ALIEN                                  #
#                                                                             #
###############################################################################
# Author:      T. Lombardi                                                    #
# Program:     hungry_alien.py                                                #
# Date:        8/9/2019                                                       #
# Version:     1.0                                                            #
# Description: The hungry alien is a simple video game designed to help       #
#              students understand the basics of software development with    #
#              the Python programming language. The module is the main driver #
#              for the game.                                                  #
###############################################################################

import sys, os
import pygame
from pygame.locals import *
from pygame.compat import geterror

#Variables to track current and data directories
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = main_dir

#Functions to create our resources (Images in this case)
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#Classes to create game sprites (characters)
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image, self.rect = load_image(image_file)
        self.rect.left, self.rect.top = location

class Alien(pygame.sprite.Sprite):
    """creates an Alien object"""
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = load_image(image_file, -1)
        self.rect.x, self.rect.y = location
        self.speed = 5

    def update(self):
        pass
     
    def left(self):
        self.rect.x -= self.speed

    def right(self):
        self.rect.x += self.speed

    def up(self):
        self.rect.y -= self.speed

    def down(self):
        self.rect.y += self.speed

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hungry Alien')

    alien = Alien("alien_green.png", [400, 300])
    BackGround = Background("Hubble_ultra_deep_field.jpg", [0,0])

    # Blit everything to the screen
    screen.blit(BackGround.image, BackGround.rect)
    screen.blit(alien.image, alien.rect)
    pygame.display.flip()

    # Main game loop
    while True:
        
        #Event handling and player updates
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    alien.left()              

        #Draw screen
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        alien.update()
        screen.blit(alien.image, alien.rect)
        pygame.display.flip()

def display_license():
    '''
    Assignment 2: Complete this function so that it prints the licensing
    information related to this project. After writing the function,
    be sure to call the function from the appropriate place in the code.
    '''
    

if __name__ == "__main__":
    main()
