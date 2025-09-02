import random
import numpy as np

class UFO:
    def __init__(self, w, h):
        # UFO can start from left or top edge, like shooting star
        if random.random() < 0.5:
            self.x = random.uniform(0, w)
            self.y = 0
            angle = random.uniform(np.pi/8, np.pi/3)
        else:
            self.x = 0
            self.y = random.uniform(0, h)
            angle = random.uniform(-np.pi/8, np.pi/8)
        # Slower than shooting star
        self.vx = np.cos(angle) * random.uniform(3, 6)
        self.vy = np.sin(angle) * random.uniform(2, 4)
        self.width = random.randint(30, 50)
        self.height = random.randint(12, 20)
        self.color = (120, 255, 120)  # Greenish UFO
        self.glow_color = (180, 255, 180)
        self.silver_color = (192, 192, 192)  # Silver disc
        self.green_light_color = (80, 255, 80)  # Bright green light
        self.green_glow_color = (180, 255, 180)  # Glow for the light
        self.active = True
        self.w = w
        self.h = h
    def update(self):
        if not self.active:
            return
        self.x += self.vx
        self.y += self.vy
        if self.x < -self.width or self.x > self.w + self.width or self.y < -self.height or self.y > self.h + self.height:
            self.active = False
    def is_alive(self):
        return self.active
