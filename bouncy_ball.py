# BOILERPLATE CODE FOR PYGAME PROJECTS
import pygame

# These are 2 libraries I have written to make drawing simple shapes easier.
from Circle import Circle
from Rectangle import Rectangle

# Initializing the pygame modules
pygame.init()
# Defining the screen width/height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
# Saving the screen to a variable
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


circle = Circle("white", 10)

# Some boolean expression for your while loop
game_over = False
# Defining the circles x speed
circle_speed_x = 1
circle_speed_y = 1

# Game loop
while not game_over:
    # Handling events (i.e. what do you want to do when the user presses w)
    for event in pygame.event.get():
        # This is something you should ALWAYS have, that states if
        # the user presses the x on the window it should close
        if event.type == pygame.QUIT:
            game_over = True

    # Logic for bouncy ball
    circle_x, circle_y = circle.get_position()
    # BOUNCING IN THE X DIRECTION
    if circle_x > (SCREEN_WIDTH - 2 * circle.get_radius()):
        circle_speed_x = -1
    elif circle_x <  0:
        circle_speed_x = 1

    if circle_y > (SCREEN_HEIGHT - 2 * circle.get_radius()):
        circle_speed_y = -1
    elif circle_y < 0:
        circle_speed_y = 1

    circle_x = circle_x + circle_speed_x  
    circle_y = circle_y + circle_speed_y

    # This is where we update stuff
    # (MOVEMENT)
    # circle_x = circle_x + 1 # 1 is your x speed
    # circle_y = circle_y + 1 # 1 is your y speed
    circle.set_position(circle_x, circle_y)

    # Clearing the screen
    screen.fill("black")

    screen.blit(circle.get_surface(), circle.get_position())
    # Displaying to the screen
    # Showing what you've drawn on the scren
    pygame.display.flip()
pygame.quit() 