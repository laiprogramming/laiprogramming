import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()

# Snake position
# tail - head
snakes = [[5,6],[5,7],[5,8]]
direction = "right"

while running:		
	clock.tick(60)
	screen.fill(BLACK)

	# Draw grid
	for i in range(21):
		pygame.draw.line(screen, WHITE,(0,i*30),(600,i*30))
		pygame.draw.line(screen, WHITE,(i*30,0),(i*30,600))

	# Draw snake
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

	# Snake move
	if direction == "right":
		snakes.append([snakes[-1][0]+1, snakes[-1][1]])
		snakes.pop(0)
	if direction == "left":
		snakes.append([snakes[-1][0]-1, snakes[-1][1]])
		snakes.pop(0)
	if direction == "up":
		snakes.append([snakes[-1][0], snakes[-1][1]-1])
		snakes.pop(0)
	if direction == "down":
		snakes.append([snakes[-1][0], snakes[-1][1]+1])
		snakes.pop(0)
	
	sleep(0.05)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"


	pygame.display.flip()

pygame.quit()