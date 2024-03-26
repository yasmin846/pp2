import pygame
pygame.init()

W, H = 500, 500
WHITE = (255,255,255)
RED = (255,0,0)

place = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
FPS = 60

x = W/2
y = H/2
speed = 20
r = 25

flLeft = flRight = flUp = flDown = False
pygame.display.set_caption("Ball")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
                x -= speed
            elif event.key == pygame.K_RIGHT:
                flRight = True
                x += speed
            elif event.key == pygame.K_UP:
                flUp = True
                y -= speed
            elif event.key == pygame.K_DOWN:
                flDown = True
                y += speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flLeft = flRight = flUp = flDown = False

    if flLeft:
        x -= speed
    elif flRight:
        x += speed
    elif flUp:
        y -= speed
    elif flDown:
        y += speed

    if x-r < 0:
        x = r
    elif x+r > W:
        x = H-r
    if y-r < 0:
        y = r
    elif y+r > W:
        y = H-r

    place.fill(WHITE)
    pygame.draw.circle(place, RED, (x, y), r)
    pygame.display.update()

    clock.tick(FPS)