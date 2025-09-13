# Hand-Controlled Particle Universe
# Copyright (C) 2025 Charles Laing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import numpy as np

class ShootingStar:
    def __init__(self, w, h):
        if random.random() < 0.5:
            self.x = random.uniform(0, w)
            self.y = 0
            angle = random.uniform(np.pi/8, np.pi/3)
        else:
            self.x = 0
            self.y = random.uniform(0, h)
            angle = random.uniform(-np.pi/8, np.pi/8)
        self.vx = np.cos(angle) * random.uniform(12, 18)
        self.vy = np.sin(angle) * random.uniform(8, 14)
        self.length = random.randint(40, 80)
        self.color = (255, 255, 200)
        self.active = True
        self.w = w
        self.h = h
    def update(self):
        if not self.active:
            return
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > self.w or self.y < 0 or self.y > self.h:
            self.active = False
    def is_alive(self):
        return self.active
