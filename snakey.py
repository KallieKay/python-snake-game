import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Snake setup
snake = [(100, 100), (90, 100), (80, 100)]
dx, dy = BLOCK_SIZE, 0

# Food
food = (
    random.randrange(0, WIDTH, BLOCK_SIZE),
    random.randrange(0, HEIGHT, BLOCK_SIZE)
)

score = 0
font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -BLOCK_SIZE
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, BLOCK_SIZE
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -BLOCK_SIZE, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = BLOCK_SIZE, 0

    # Move snake
    head = snake[0]
    new_head = (head[0] + dx, head[1] + dy)
    snake.insert(0, new_head)

    # Food collision
    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        )
    else:
        snake.pop()

    # Wall collision
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        running = False

    # Self collision
    if new_head in snake[1:]:
        running = False

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    # Draw score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()