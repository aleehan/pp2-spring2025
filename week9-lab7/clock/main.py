import pygame
import datetime
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

myClock = pygame.image.load("clock.png")
right_hand = pygame.image.load("min_hand.png")
left_hand = pygame.image.load("sec_hand.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    current_time = datetime.datetime.now()
    current_min = current_time.strftime("%M")
    current_sec = current_time.strftime("%S")

    angle_min = -6 * int(current_min)
    angle_sec = -6 * int(current_sec)

    minute = pygame.transform.rotate(right_hand, angle_min)
    second = pygame.transform.rotate(left_hand, angle_sec)

    rect = minute.get_rect(center=(400, 300))
    rect2 = second.get_rect(center=(400, 300))

    screen.fill((0, 0, 0))
    screen.blit(myClock, (0, 0))
    screen.blit(minute, rect)
    screen.blit(second, rect2)

    pygame.display.update()
    clock.tick(60)

