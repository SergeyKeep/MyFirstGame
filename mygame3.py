import pygame
import random
import os
import menu2

from PyQt5.QtWidgets import QApplication


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
    count1 = 0
    pygame.init()
    size = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    SPAWNTARGET = 30
    pygame.time.set_timer(SPAWNTARGET, 150)

    all_sprites = pygame.sprite.Group()

    backround = pygame.sprite.Sprite(all_sprites)
    backround.image = load_image("space.png")
    backround.rect = backround.image.get_rect()
    backround.rect.x = 0
    backround.rect.y = 0

    player = pygame.sprite.Sprite()
    player.image = load_image("astrominer.png")
    player.rect = player.image.get_rect()
    all_sprites.add(player)
    player.mask = pygame.mask.from_surface(player.image)
    WHITE = (0, 255, 255)

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
                bullet = pygame.sprite.Sprite(all_sprites)
                bullet.image = load_image("bullet.jpg")
                bullet.rect = bullet.image.get_rect()
                bullet.rect.x = event.pos[0]
                bullet.rect.y = event.pos[1]
                circles.append(bullet)
                bullet.mask = pygame.mask.from_surface(bullet.image)

            if event.type == SPAWNTARGET:
                meteor = pygame.sprite.Sprite(all_sprites)
                meteor.image = load_image("aster.jpg")
                meteor.rect = meteor.image.get_rect()
                meteor.rect.x = random.randint(x_min, x_max)
                meteor.rect.y = 0
                targets.append(meteor)
                meteor.mask = pygame.mask.from_surface(meteor.image)

        meteor_delete = []
        bullet_delete = []

        for i, target in enumerate(targets):
            if pygame.sprite.collide_mask(player, target):
                running = False
            hit = False
            for bullet in circles:
                if pygame.sprite.collide_mask(bullet, target):
                    hit = True

            if hit:
                target.kill()
                meteor_delete.append(i)
                count1 += 1

        screen.fill((0, 0, 0))

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            player.rect.x = pos[0] - 20
            player.rect.y = pos[1] - 35

        for i, circle_center in enumerate(circles):
            circle_center.rect.y -= 15
            if circle_center.rect.y < -50:
                bullet_delete.append(i)

        for i, target_pos in enumerate(targets):
            target_pos.rect.y += 3
            if target_pos.rect.y > 400:
                meteor_delete.append(i)

        for i, j in enumerate(list(set(meteor_delete))):
            targets.pop(j - i)
        for i, j in enumerate(bullet_delete):
            circles.pop(j - i)
        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)

    app = QApplication([])
    end_menu = menu2.MainWindow(count1)
    end_menu.show()
    app.exec()

    pygame.quit()
    return count1


if __name__ == "__main__":
    run_game()
