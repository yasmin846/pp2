import pygame
pygame.init()


W, H = 1080, 1916
place = pygame.display.set_mode(W,H)
speed = 5
score = 0

back = pygame.image.load('road.png')
car = pygame.image.load('car.png')
enemy = pygame.image.load('enemy.png')
crash = pygame.sound
place = pygame.display.set_mode(W,H)
pygame.display.set_caption('Racer')

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


clock.tick(FPS)