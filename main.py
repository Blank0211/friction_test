import sys
import pygame as pg
vec2 = pg.math.Vector2

# Colours
black = (0, 0, 0)
blue1 = pg.Color("#197bd2")
red = pg.Color("#f04c64")

# Display
width, height = 640, 480
FPS = 120
win = pg.display.set_mode((width, height))
pg.display.set_caption("friction")
clock = pg.time.Clock()

# Sprites
class Player(pg.sprite.Sprite):
    def __init__(self, color, size, pos):
        self.pos = vec2(pos)
        self.vel = vec2(0, 0)
        self.acc = vec2(0, 0)
        self.fric = 0.98
        self.max_speed = 8

        self.image = pg.Surface(size)
        self.rect = self.image.get_rect(center=pos)
        self.image.fill(red)

    def update(self, dt):
        self.acc = vec2(0, 0)
        keys = pg.key.get_pressed()

        # Redeploy if out of boundaries
        if self.rect.left > width:
            self.pos.x = 0 - 9
        if self.rect.right < 0:
            self.pos.x = width + 9

        if keys[pg.K_RIGHT]:
            self.acc.x += 10
        elif keys[pg.K_LEFT]:
            self.acc.x -= 10

        self.vel += self.acc
        self.vel *= self.fric
        self.pos += self.vel * dt

        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def draw(self, win):
        win.blit(self.image, self.rect)


p1 = Player(red, (18, 36), (width//2, height//2))

# Game Loop
def main():
    pg.init()

    running = True
    while running:
        # limit FPS and get delta time
        dt = clock.tick(FPS) / 1000
        
        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update & draw sprites
        p1.update(dt)
        win.fill(black) # Clear background
        p1.draw(win)

        # Update Display
        pg.display.flip()

    # Post loop
    pg.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
