import pygame


class Card:
    def __init__(self, image, color, number, type):
        self.image = pygame.image.load(image)
        self.color = color
        self.number = number
        self.type = type


a = Card(image="y41.png", color="yellow", number=4, type="attack")


class AttackCard(Card):
    def __init__(self, image, color, number):
        super().__init__(image, color, number)
