# Bouncing Balls Program
# Step 4/7: Bounce the ball 
# Lai Programming - Watch Full Tutorial: https://youtu.be/W9fdczla2ds
import pygame
import numpy as np
import math
pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255,0,0)
CIRCLE_CENTER = np.array([WIDTH / 2, HEIGHT / 2],dtype=np.float64)
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = np.array([WIDTH // 2, HEIGHT // 2 - 120],dtype=np.float64)
ball_vel = np.array([0, 0],dtype=np.float64)
gravity = 0.2
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	ball_vel[1] += gravity
	ball_pos += ball_vel
	dist = np.linalg.norm(ball_pos-CIRCLE_CENTER)
	if dist + BALL_RADIUS > CIRCLE_RADIUS:
		d = ball_pos - CIRCLE_CENTER
		d_unit = d/np.linalg.norm(d)
		t = np.array([-d[1], d[0]], dtype=np.float64)
		ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit
		proj_v_t = (np.dot(ball_vel, t) / np.dot(t, t)) * t 
		ball_vel = 2 * proj_v_t - ball_vel 
	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
	pygame.draw.circle(window, RED, (ball_pos[0],ball_pos[1]), BALL_RADIUS)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()