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

