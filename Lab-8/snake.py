import pygame
import random
import time

pygame.init()

HEIGHT, WIDTH=600,600
CELL=30
screen=pygame.display.set_mode((WIDTH,HEIGHT))
WHITE=(255,255,255)
GRAY=(255,200,200)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BlUE=(0,0,255)
Yellow=(255,255,0)

def draw_grid_chess():
    colors=[WHITE,GRAY]
    for i in range(HEIGHT//2):
        for j in range(WIDTH//2):
            pygame.draw.rect(screen,colors[(i+j)%2],(i*CELL, j*CELL, CELL, CELL))

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.grow = False

    def move(self):
        if self.grow:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.grow = False
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, Yellow, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow = True
            return True
        return False

    def check_self_collision(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

class Food:
    def __init__(self):
        self.randomize()
        self.spawn_time = time.time()

    def randomize(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.value = random.choice([1, 2, 3])  #weight of food
        self.spawn_time = time.time()

    def draw(self):
        color = GREEN if self.value == 1 else BlUE if self.value == 2 else RED
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def expired(self):
        return time.time() - self.spawn_time > 5  #dissappers asfter 5 second


def draw_text(text, x, y, color):
    font = pygame.font.Font(None, 36)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()
food = Food()
snake = Snake()

game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")

running = True
while running:
    screen.fill(BLACK)
    draw_grid_chess()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    snake.move()
    
    if snake.check_self_collision() or snake.check_wall_collision():
        screen.fill(BLACK)
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    if snake.check_collision(food):
        score += food.value  #если вес больше то размер тоже становится больше
        food.randomize()
        if score % 4 == 0:
            level += 1
            FPS += 1

    if food.expired():
        food.randomize()

    snake.draw()
    food.draw()
    draw_text(f"Score: {score}", 10, 10, BLACK)
    draw_text(f"Level: {level}", 10, 40, BLACK)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


