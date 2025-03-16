import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

ball_color = (255, 0, 0)
ball_x = 500 // 2
ball_y = 500 // 2
ball_radius = 25
ball_movement = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_x = min(500 - ball_radius, ball_x + ball_movement)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_radius, ball_x - ball_movement)
            elif event.key == pygame.K_UP:
                ball_y = max(ball_radius, ball_y - ball_movement)
            elif event.key == pygame.K_DOWN:
                ball_y = min(500 - ball_radius, ball_y + ball_movement)

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    pygame.display.update()
    clock.tick(60)
