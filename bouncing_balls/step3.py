# Bouncing Balls Program
# Step 3/7: Drop the ball
# Lai Programming - Watch Full Tutorial: https://youtu.be/W9fdczla2ds
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255,0,0)
CIRCLE_CENTER = [WIDTH // 2, HEIGHT // 2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
GRAVITY = 0.2
ball_pos = [WIDTH // 2, HEIGHT // 2 - 120]
ball_vel = [0, 0]
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	ball_vel[1] += GRAVITY
	ball_pos[0] += ball_vel[0]
	ball_pos[1] += ball_vel[1]
	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
	pygame.draw.circle(window, RED, (ball_pos[0],ball_pos[1]), BALL_RADIUS)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()