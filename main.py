import pygame

# Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game - Shawn Humphreys!")

# Game variables
hangman_status = 4

# Colors
WHITE = (255,255,255)

# Load images
images = []
for i in range(6):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)


# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

# Exit
while run:
    clock.tick(FPS)

    win.fill((WHITE))
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()
