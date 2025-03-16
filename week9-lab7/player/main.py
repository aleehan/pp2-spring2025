import pygame
import os
from sys import exit

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Fishofy")
clock = pygame.time.Clock()

music_path = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week9-lab7\player\playlist"

playlist = []
for file in os.listdir(music_path):
    if file.endswith(".ogg"):
        playlist.append(file)

current_music = 0
paused = False

font_path = r"C:\Users\lesh\Desktop\Work\fonts\montserrat"
font = pygame.font.Font(os.path.join(font_path, "Montserrat-Medium.ttf"), 16)

cat = pygame.image.load("cat2.jpg")
instruction = pygame.image.load("instrustion.png")

names_without_extension = []
for name in playlist:
    names_without_extension.append(name.rsplit(".", 1)[0])


pygame.mixer.music.load(os.path.join(music_path, playlist[current_music]))
pygame.mixer.music.play(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            if event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_path, playlist[current_music]))
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_path, playlist[current_music]))
                pygame.mixer.music.play()

    screen.fill((0,0,0))

    screen.blit(cat, (0, 0))

    text_surface = font.render(names_without_extension[current_music].center(0), True, (0, 171, 255))
    screen.blit(text_surface, (230, 25))
    screen.blit(instruction, (0, 0))

    pygame.display.update()
    clock.tick(60)