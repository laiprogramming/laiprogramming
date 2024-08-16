# Bouncing Balls Program
# Step 6/7: Drop ball out of circle
# Lai Programming - Watch Full Tutorial: https://youtu.be/W9fdczla2ds
import pygame
import numpy as np
import math
def is_ball_in_arc(ball_pos, CIRCLE_CENTER, start_angle, end_angle):
    dx = ball_pos[0] - CIRCLE_CENTER[0]
    dy = ball_pos[1] - CIRCLE_CENTER[1]
    ball_angle = math.atan2(dy, dx)
    start_angle = start_angle % (2 * math.pi)
    end_angle = end_angle % (2 * math.pi)
    if start_angle > end_angle:
        end_angle += 2 * math.pi
    if start_angle <= ball_angle <= end_angle or (start_angle <= ball_angle + 2 * math.pi <= end_angle): # Check if the ball's angle is within the arc's angular range
        return True
    return False
def draw_arc(window, color, center, radius, start_angle, end_angle):
	p1 = center + (radius+1000) * np.array([math.cos(start_angle),math.sin(start_angle)])
	p2 = center + (radius+1000) * np.array([math.cos(end_angle),math.sin(end_angle)])
	pygame.draw.polygon(window,color, [center,p1,p2], 0)
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
GRAVITY = 0.2
SPINNING_SPEED = 0.01
ARC_DEGREE = 60
start_angle = math.radians(-ARC_DEGREE / 2)
end_angle = math.radians(ARC_DEGREE / 2)
is_ball_in = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	start_angle += SPINNING_SPEED
	end_angle += SPINNING_SPEED
	ball_vel[1] += GRAVITY
	ball_pos += ball_vel
	dist_to_CIRCLE_CENTER = math.hypot(ball_pos[0] - CIRCLE_CENTER[0], ball_pos[1] - CIRCLE_CENTER[1])
		if is_ball_in_arc(ball_pos, CIRCLE_CENTER, start_angle, end_angle):
			is_ball_in = False
		if is_ball_in:
			d = ball_pos - CIRCLE_CENTER
			d_norm = math.hypot(d[0], d[1])
			d_unit = d/d_norm
			t = np.array([-d[1], d[0]], dtype=np.float64)
			ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit
			proj_v_t = (np.dot(ball_vel, t) / np.dot(t, t)) * t
			ball_vel = 2 * proj_v_t - ball_vel
			ball_vel += t * SPINNING_SPEED
	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
	draw_arc(window, BLACK, CIRCLE_CENTER, CIRCLE_RADIUS, start_angle, end_angle)
	pygame.draw.circle(window, RED, (ball_pos[0],ball_pos[1]), BALL_RADIUS)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()