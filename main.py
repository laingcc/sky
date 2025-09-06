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

import cv2
import mediapipe as mp
import numpy as np
import random
import time
from particle import Particle
from background_particle import BackgroundParticle
from shooting_star import ShootingStar
from ufo import UFO
from screeninfo import get_monitors

mp_hands = mp.solutions.hands

# Get screen size
monitor = get_monitors()[1]
screen_w, screen_h = monitor.width, monitor.height

# --- Helper Functions ---
def update_and_draw_background_particles(universe, background_particles, w, h):
    if background_particles is None:
        background_particles = [BackgroundParticle(w, h) for _ in range(100)]
    for bp in background_particles:
        bp.update(w, h)
        cv2.circle(universe, (int(bp.x), int(bp.y)), bp.radius, bp.color, -1)
    return background_particles

def get_hand_positions(results, w, h):
    hand_positions = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark[0]
            x, y = int(lm.x * w), int(lm.y * h)
            hand_positions.append((x, y))
    return hand_positions

def emit_particles_from_hands(hand_positions, particles, now, last_emit, emit_interval):
    # Lower number of particles emitted per hand
    if hand_positions and now - last_emit > emit_interval:
        for x, y in hand_positions:
            for _ in range(random.randint(2, 4)):
                particles.append(Particle(x, y, 'star'))
            if random.random() < 0.2:
                particles.append(Particle(x, y, 'galaxy'))
        last_emit = now
    return particles, last_emit

def update_and_draw_particles(universe, particles):
    new_particles = []
    overlay_needed = any(p.kind != 'star' for p in particles)
    overlay = None
    if overlay_needed:
        overlay = universe.copy()
    for p in particles:
        p.update()
        if p.is_alive():
            if p.kind == 'star':
                cv2.circle(universe, (int(p.x), int(p.y)), p.radius, p.color, -1)
            else:
                if overlay is not None:
                    cv2.circle(overlay, (int(p.x), int(p.y)), p.radius, p.color, -1)
            new_particles.append(p)
    if overlay is not None:
        alpha = 0.2
        cv2.addWeighted(overlay, alpha, universe, 1 - alpha, 0, universe)
    return new_particles

def update_and_draw_shooting_stars(universe, shooting_stars, w, h):
    # Lower spawn probability for performance
    if random.random() < 0.002:
        shooting_stars.append(ShootingStar(w, h))
    new_shooting_stars = []
    for star in shooting_stars:
        star.update()
        if star.is_alive():
            x2 = int(star.x - star.vx * star.length / 20)
            y2 = int(star.y - star.vy * star.length / 20)
            cv2.line(universe, (int(star.x), int(star.y)), (x2, y2), star.color, 2)
            new_shooting_stars.append(star)
    return new_shooting_stars

def update_and_draw_ufos(universe, ufo_list, w, h):
    # Lower spawn probability for performance
    if random.random() < 0.00005:
        ufo_list.append(UFO(w, h))
    new_ufo_list = []
    overlay = None
    for ufo in ufo_list:
        ufo.update()
        if ufo.is_alive():
            cv2.ellipse(universe, (int(ufo.x), int(ufo.y)), (ufo.width, ufo.height), 0, 0, 360, ufo.silver_color, -1)
            if overlay is None:
                overlay = universe.copy()
            cv2.ellipse(overlay, (int(ufo.x), int(ufo.y - ufo.height//2)), (ufo.width//4, ufo.height//3), 0, 0, 360, ufo.green_glow_color, -1)
            cv2.ellipse(universe, (int(ufo.x), int(ufo.y - ufo.height//2)), (ufo.width//6, ufo.height//6), 0, 0, 360, ufo.green_light_color, -1)
            new_ufo_list.append(ufo)
    if overlay is not None:
        cv2.addWeighted(overlay, 0.5, universe, 0.5, 0, universe)
    return new_ufo_list

def main():
    # --- Main Loop ---
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Universe - Hands Emit Galaxies & Stars', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Universe - Hands Emit Galaxies & Stars', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    particles = []
    last_emit = 0
    emit_interval = 0.05
    frame_count = 0
    cloud_mask = None
    background_particles = None
    shooting_stars = []
    ufo_list = []

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break
            # Resize camera frame to universe size for hand detection
            frame_resized = cv2.resize(frame, (screen_w, screen_h), interpolation=cv2.INTER_LINEAR)
            universe = np.zeros((screen_h, screen_w, 3), dtype=np.uint8)
            background_particles = update_and_draw_background_particles(universe, background_particles, screen_w, screen_h)
            frame_count += 1
            rgb_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)
            hand_positions = get_hand_positions(results, screen_w, screen_h)
            now = time.time()
            particles, last_emit = emit_particles_from_hands(hand_positions, particles, now, last_emit, emit_interval)
            particles = update_and_draw_particles(universe, particles)
            shooting_stars = update_and_draw_shooting_stars(universe, shooting_stars, screen_w, screen_h)
            ufo_list = update_and_draw_ufos(universe, ufo_list, screen_w, screen_h)
            cv2.imshow('Universe - Hands Emit Galaxies & Stars', universe)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
