import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, alien_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.screen_rect = alien_game.screen.get_rect()

        # load the ship image amd get its rect.
        self.image = pygame.image.load('images/transport.png')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #  Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        #  Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitMe(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
