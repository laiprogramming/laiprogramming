import pygame

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

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				snakes.append([snakes[-1][0], snakes[-1][1]-1])
				snakes.pop(0)
			if event.key == pygame.K_DOWN:
				snakes.append([snakes[-1][0], snakes[-1][1]+1])
				snakes.pop(0)
			if event.key == pygame.K_LEFT:
				snakes.append([snakes[-1][0]-1, snakes[-1][1]])
				snakes.pop(0)
			if event.key == pygame.K_RIGHT:
				snakes.append([snakes[-1][0]+1, snakes[-1][1]])
				snakes.pop(0)
				
	pygame.display.flip()

pygame.quit()