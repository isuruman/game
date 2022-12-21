import pygame

# Initialize pygame
pygame.init()

# Set the window size
WIDTH = 400
HEIGHT = 400

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption('My Game')

# Set the sprite's starting position
x = 50
y = 50

# Set the sprite's movement speed
speed = 5

# Set the goal position
goal_x = 350
goal_y = 350

# Set the game state (win or lose)
game_state = 'playing'

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the user's input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Update the game state
    if game_state == 'playing':
        if x == goal_x and y == goal_y:
            game_state = 'win'
    elif game_state == 'win':
        # Display the win screen
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render('You Win!', True, (0, 0, 0))
        screen.blit(text, (WIDTH / 2, HEIGHT / 2))
        pygame.display.flip()
    elif game_state == 'lose':
        # Display the lose screen
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render('You Lose!', True, (0, 0, 0))
        screen.blit(text, (WIDTH / 2, HEIGHT / 2))
        pygame.display.flip()

    # Draw the sprite
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)
    pygame.draw.circle(screen, (255, 0, 0), (goal_x, goal_y), 10)
    pygame.display.flip()
