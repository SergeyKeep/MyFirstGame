import pygame
import random

def run_game():
    pygame.init()
    size = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    SPAWN_TARGET = 30
    pygame.time.set_timer(SPAWN_TARGET, 1000)

    x_min, x_max = 0, 600

    v = 20
    fps = 60
    targets = []
    circles = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == SPAWN_TARGET:
                targets.append([random.randint(x_min, x_max), 0])


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, (255, 0, 0), circle_center[1], 2)

        screen.fill((0, 0, 0))
        for target_pos in targets:
            target_pos[1] += 1
            pygame.draw.circle(screen, (255, 0, 0), target_pos, 20)
        for circle_center in circles:
            circle_center[1] += 1
            pygame.draw.circle(screen, (255, 0, 0), circle_center, 20)

        pygame.display.update()
        clock.tick(30)

run_game()
