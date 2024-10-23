import curses
import math
import time
import pygame

def move_sphere(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        stdscr.clear()
        run_sphere_animation()
        stdscr.refresh()


def run_sphere_animation():

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set window size
    clock = pygame.time.Clock()  # Frame rate control
    radius = 30  # Sphere radius

    # Create a pygame.Rect object representing the player (as a bounding box for the sphere)
    player = pygame.Rect(400, 300, radius * 2, radius * 2)  # (x, y, width, height)

    # Set up initial velocity
    vx, vy = 5, 3  # Velocity in x and y directions
    friction = 0.99  # Friction for smooth movement
    acceleration = 0.1  # Acceleration factor for direction changes

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black color

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # Check for key presses

        # Update velocity based on key presses for smooth direction changes
        if keys[pygame.K_UP]:
            vy -= acceleration
        if keys[pygame.K_DOWN]:
            vy += acceleration
        if keys[pygame.K_LEFT]:
            vx -= acceleration
        if keys[pygame.K_RIGHT]:
            vx += acceleration

        # Update position
        player.x += vx
        player.y += vy

        # Boundary collision detection and realistic bouncing
        if player.right >= screen.get_width() or player.left <= 0:
            vx = -vx * friction  # Reverse velocity and apply friction
        if player.bottom >= screen.get_height() or player.top <= 0:
            vy = -vy * friction

        # Draw the sphere as a circle inside the player's rectangle
        pygame.draw.circle(screen, (255, 0, 0), player.center, radius)

        # Update the display and maintain frame rate
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    curses.wrapper(move_sphere)
