import pygame
import random
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def run_game():
    pygame.init()
    size = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    SPAWNTARGET = 30
    pygame.time.set_timer(SPAWNTARGET, 1000)
    image = pygame.sprite.Sprite(load_image("astrominer.png"))

    WHITE = (0, 255, 255)
    BLUE = (0, 0, 225)

    x_min, x_max = 0, 600
    circles = []
    targets = []
    pygame.mouse.set_visible(False)
    sc = pygame.display.set_mode((400, 300))

    sc.fill(WHITE)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                circles.append(list(event.pos))
            if event.type == SPAWNTARGET:
                targets.append([random.randint(x_min, x_max), 0])



        screen.fill((0, 0, 0))

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            image.draw()

        for circle_center in circles:
            circle_center[1] -= 15
            pygame.draw.circle(screen, (255, 0, 0), circle_center, 1)
        for target_pos in targets:
            target_pos[1] += 1
            pygame.draw.circle(screen, (255, 0, 0), target_pos, 20)

        pygame.display.update()
        clock.tick(30)

run_game()
