import pygame

black = (0, 0, 0)
white = (255,  255, 255)

pygame.init()

size = 700,500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()

def ball(x,y):
    pygame.draw.circle(screen, black, [x,y], 20)

x = 350
y = 250
x_speed = 0
y_speed = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 3

    screen.fill(white)
    ball(x,y)

    y += y_speed

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


