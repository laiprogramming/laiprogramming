# Bouncing Balls Program
# Step 5/7: Spin the circle (Draw spinning arc and Add tangential force)
# Lai Programming - Watch Full Tutorial: https://youtu.be/W9fdczla2ds
import pygame
import numpy as np
import math
def draw_arc(window, center, radius, start_angle, end_angle):
	p1 = center + (radius+1000) * np.array([math.cos(start_angle),math.sin(start_angle)])
	p2 = center + (radius+1000) * np.array([math.cos(end_angle),math.sin(end_angle)])
	pygame.draw.polygon(window,BLACK, [center,p1,p2], 0)
pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255,0,0)
CIRCLE_CENTER = np.array([WIDTH // 2, HEIGHT // 2],dtype=np.float64)
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = np.array([WIDTH // 2, HEIGHT // 2 - 120],dtype=np.float64)
ball_vel = np.array([0, 0],dtype=np.float64)
gravity = 0.2
spinning_speed = 0.01 
arc_degrees = 60
start_angle = math.radians(-arc_degrees / 2)  
end_angle = math.radians(arc_degrees / 2)     
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	start_angle += spinning_speed
	end_angle += spinning_speed
	ball_vel[1] += gravity
	ball_pos += ball_vel
	dist = np.linalg.norm(ball_pos-CIRCLE_CENTER)
	if dist + BALL_RADIUS > CIRCLE_RADIUS:
		d = ball_pos - CIRCLE_CENTER
		d_norm = math.hypot(d[0], d[1])
		d_unit = d/d_norm
		t = np.array([-d[1], d[0]], dtype=np.float64) 
		ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit 
		proj_v_t = (np.dot(ball_vel, t) / np.dot(t, t)) * t 
		ball_vel = 2 * proj_v_t - ball_vel 
		ball_vel += t * spinning_speed 
	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
	draw_arc(window, CIRCLE_CENTER, CIRCLE_RADIUS, start_angle, end_angle)
	pygame.draw.circle(window, RED, (ball_pos[0],ball_pos[1]), BALL_RADIUS)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()