import pygame
import os
pygame.init()

pygame.display.set_caption('Music Player')
W, H = 300, 200
screen = pygame.display.set_mode((W,H))

Song = []
for f in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), f)) and f.endswith(".mp3"):
        Song.append(f)
s = 0
pygame.mixer.music.load(Song[s])
pygame.mixer.music.play()

paused = False
Song1 =[]
a = 1
for i in Song:
    Song1.append(Song[len(Song)-a])
    a += 1 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                s = (s + 1) % len(Song)
                pygame.mixer.music.load(Song[s])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                s = (s - 1) % len(Song)
                pygame.mixer.music.load(Song[s])
                pygame.mixer.music.play()

    screen.fill((0,0,0))
    pygame.display.update()