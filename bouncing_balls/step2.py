# Bouncing Balls Program
# Step 2/7: Draw circle and ball
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
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = [WIDTH/2, HEIGHT/2 - 120]
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	window.fill(BLACK)
	pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
	pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()

104333137 Mannamarakkalage Geenodh Risinu Cooray
101926301 Liam Joyce
104093910 Pulkit Pannu
7696663 Joshua Stone
104220556 Khang Vo
104792990 Rajasinghe Keshini Munasinghe