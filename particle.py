import random

class Particle:
    def __init__(self, x, y, kind):
        self.x = x + random.randint(-10, 10)
        self.y = y + random.randint(-10, 10)
        self.kind = kind  # 'star' or 'galaxy'
        self.radius = random.randint(1, 3) if kind == 'star' else random.randint(8, 16)
        if kind == 'star':
            color_choices = [
                (255, 255, 255), # white
                (255, 255, 0),   # yellow
                (0, 255, 255),   # cyan
                (255, 0, 255),   # magenta
                (0, 255, 0),     # green
                (0, 0, 255),     # blue
                (255, 0, 0),     # red
                (255, 128, 0),   # orange
                (128, 0, 255),   # purple
            ]
            self.color = random.choice(color_choices)
        else:
            self.color = (
                random.randint(128,255),
                random.randint(64,255),
                random.randint(128,255)
            )
        self.life = random.randint(30, 80) if kind == 'star' else random.randint(60, 120)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        if self.kind == 'galaxy':
            r, g, b = self.color
            self.color = (
                min(255, max(0, r + random.randint(-2, 2))),
                min(255, max(0, g + random.randint(-2, 2))),
                min(255, max(0, b + random.randint(-2, 2)))
            )

    def is_alive(self):
        return self.life > 0

