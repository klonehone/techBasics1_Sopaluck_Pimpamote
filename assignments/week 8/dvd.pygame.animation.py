import pygame
import random

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

class DVD:
    def __init__(self):
        img = pygame.image.load("dvd.png")
        self.img = pygame.transform.scale(img, (120, 70))
        # random starting position
        self.pos_x = random.randint(0, SCREEN_WIDTH - 120)
        self.pos_y = random.randint(0, SCREEN_HEIGHT - 70)
        # random speed and direction
        self.speed_x = random.choice([-1, 1]) * random.randint(2, 4)
        self.speed_y = random.choice([-1, 1]) * random.randint(2, 4)
        # random starting color
        self.color = self.random_color()

    def random_color(self):
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def tint(self):
        # apply color tint to the image copy
        tinted = self.img.copy()
        tinted.fill(self.color, special_flags=pygame.BLEND_MULT)
        return tinted

    def animate(self):
        hit_wall = False

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        # bounce off left and right walls
        if self.pos_x <= 0 or self.pos_x >= SCREEN_WIDTH - 120:
            self.speed_x *= -1
            hit_wall = True

        # bounce off top and bottom walls
        if self.pos_y <= 0 or self.pos_y >= SCREEN_HEIGHT - 70:
            self.speed_y *= -1
            hit_wall = True

        # change color on bounce
        if hit_wall:
            self.color = self.random_color()

    def draw(self):
        tinted = self.tint()
        screen.blit(tinted, (self.pos_x, self.pos_y))


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DVD Screensaver")

# create one dvd logo
dvd = DVD()

clock = pygame.time.Clock()

flag = True
while flag:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.fill(BACKGROUND_COLOR)

    dvd.animate()
    dvd.draw()

    pygame.display.flip()

pygame.quit()
exit(0)
