import pygame

pygame.init()

width,height=600, 400
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakey Game")

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

pygame.quit()

snake = [(100, 100), (90, 100), (80, 100)]
snake_size=10

for segment in snake:
    pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], snake_size, snake_size ))

    