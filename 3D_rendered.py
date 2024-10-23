import pygame

def run_sphere_animation():
    # Initialize pygame and set up the screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set window size
    clock = pygame.time.Clock()  # Frame rate control
    radius = 30  # Sphere radius

    # Set up initial position and velocity
    x, y = screen.get_width() // 2, screen.get_height() // 2
    vx, vy = 0, 0  # Initial velocity in x and y directions
    acceleration = 0.1  # Acceleration factor for direction changes
    friction = 0.98  # Friction to slow down movement

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # Check for key presses
        #
        # # Update velocity based on key presses for smooth direction changes
        # if keys[pygame.K_UP]:
        #     vy -= acceleration
        # if keys[pygame.K_DOWN]:
        #     vy += acceleration
        # if keys[pygame.K_LEFT]:
        #     vx -= acceleration
        # if keys[pygame.K_RIGHT]:
        #     vx += acceleration
        #
        # # Apply friction to slow down gradually
        # vx *= friction
        # vy *= friction

        # Update position
        x += vx
        y += vy

        # Boundary collision detection and realistic bouncing
        if x + radius >= screen.get_width() or x - radius <= 0:
            vx = -vx * friction  # Reverse velocity and apply friction
            x = min(max(x, radius), screen.get_width() - radius)  # Ensure the sphere stays within bounds
        if y + radius >= screen.get_height() or y - radius <= 0:
            vy = -vy * friction
            y = min(max(y, radius), screen.get_height() - radius)  # Ensure the sphere stays within bounds

        # Clear screen with black color
        screen.fill((0, 0, 0))

        # Draw the sphere
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)

        # Update the display and maintain frame rate
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    run_sphere_animation()
