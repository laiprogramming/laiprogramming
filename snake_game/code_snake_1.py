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
snake = [19,19]

while running:		
	clock.tick(60)
	screen.fill(BLACK)

	# Draw grid
	for i in range(21):
		pygame.draw.line(screen, WHITE,(0,i*30),(600,i*30))
		pygame.draw.line(screen, WHITE,(i*30,0),(i*30,600))

	pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				snake[1] -= 1
			if event.key == pygame.K_DOWN:
				snake[1] += 1
			if event.key == pygame.K_LEFT:
				snake[0] -= 1
			if event.key == pygame.K_RIGHT:
				snake[0] += 1
				
	pygame.display.flip()

pygame.quit()