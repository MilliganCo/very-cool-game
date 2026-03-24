import pygame
import sys
import random

# Game setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool RPG Game")

# Colors
WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
BLACK = (0, 0, 0)

# Player setup
player_size = 40
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5
player_health = 100

# Enemy setup
enemy_size = 40
enemy_pos = [random.randint(0, WIDTH-enemy_size), random.randint(0, HEIGHT-enemy_size)]

# Fonts
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 56)

def draw_text(text, font, color, surface, x, y):
    t = font.render(text, True, color)
    surface.blit(t, (x, y))

def draw_game():
    screen.fill(BLACK)
    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    # Draw health bar
    pygame.draw.rect(screen, RED, (10, 10, 100, 20))
    pygame.draw.rect(screen, GREEN, (10, 10, player_health, 20))
    # Title and controls
    draw_text("COOL RPG GAME", big_font, WHITE, screen, 200, 50)
    draw_text("Arrow Keys/WASD to move, Q to quit", font, WHITE, screen, 200, 100)
    pygame.display.flip()

def move_enemy():
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += 2
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= 2
    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += 2
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= 2

def check_collision():
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    return player_rect.colliderect(enemy_rect)

def show_game_over():
    screen.fill(BLACK)
    draw_text("GAME OVER", big_font, RED, screen, WIDTH//2-120, HEIGHT//2-40)
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    global player_health
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # Keyboard state for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_pos[1] += player_speed

        # Player bounds
        player_pos[0] = max(0, min(player_pos[0], WIDTH-player_size))
        player_pos[1] = max(0, min(player_pos[1], HEIGHT-player_size))

        # Enemy acts
        move_enemy()

        # Check for collision
        if check_collision():
            player_health -= 1

        # Game over
        if player_health <= 0:
            show_game_over()
            running = False

        draw_game()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()