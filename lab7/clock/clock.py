import pygame
from datetime import datetime
pygame.init()

W, H = 900, 890
WHITE = (255, 255, 255)
place = pygame.display.set_mode((W,H))
mid = W/2, H/2

back = pygame.image.load('mainclock.png')
sec = pygame.image.load('leftarm.png')
min = pygame.image.load('rightarm.png')

clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption('Mickey Mouse Clock')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    time = datetime.now()
    sec1 = (time.second / 60) * 360
    min1 = (time.minute / 60) * 360 + (time.second / 60) * (360 / 60)

    rtLeft = pygame.transform.rotate(sec, - sec1)
    rcLeft = rtLeft.get_rect(center = mid)
    rtRight = pygame.transform.rotate(min, -min1)
    rcRight = rtRight.get_rect(center = mid)

    place.fill(WHITE)
    place.blit(back, (0, 0))
    place.blit(rtLeft, rcLeft)
    place.blit(rtRight, rcRight)
    pygame.display.update()
    clock.tick(FPS)