import pygame

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
clock = pygame.time.Clock()

while running:		
	clock.tick(60)
	screen.fill(GREEN)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()