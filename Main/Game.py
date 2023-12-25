import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Các hằng số
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tạo màn hình game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Tạo đối tượng xe
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xử lý sự kiện di chuyển
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
        car_x += 5

    # Vẽ màn hình
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt tốc độ khung hình
    clock.tick(60)
