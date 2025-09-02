import random

class BackgroundParticle:
    def __init__(self, w, h):
        self.x = random.uniform(0, w)
        self.y = random.uniform(0, h)
        self.vx = random.uniform(-0.2, 0.2)
        self.vy = random.uniform(-0.2, 0.2)
        self.radius = random.randint(1, 2)
        self.color = (random.randint(80,180), random.randint(80,180), random.randint(120,255))

    def update(self, w, h):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0: self.x += w
        if self.x > w: self.x -= w
        if self.y < 0: self.y += h
        if self.y > h: self.y -= h

