import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""
    def __init__(self, ai_game):
        super().__init__()
        """Initialize the ship and set it's starting porition"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # self.bg_color = self.settings.bg_color

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.center = self.screen_rect.center

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)