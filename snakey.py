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


"""think of the snake as a list of blocks"""
snake = [(100, 100), (90, 100), (80, 100)]
snake_size=10

"""drawing the snake"""
for segment in snake:
    pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], snake_size, snake_size ))

"""using direction variables for movement"""
dx=10
dy=0

"""update snake position each frame"""
head=snake[0]
new_head=(head[0]+dx, head[1]+dy)
snake.insert(0, new_head)
snake.pop()

"""keyboard controls"""
keys=pygame.key.get_pressed()

if keys[pygame.K_UP]:
    dx, dy =0, -10
elif keys[pygame.K_DOWN]:
    dx, dy= 0, 10
elif keys[pygame.K_LEFT]:
    dx, dy= -10, 0
elif keys[pygame.K_RIGHT]:
    dx, dy=10, 0

"""adding food"""

