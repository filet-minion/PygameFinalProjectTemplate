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
# Defining a clock to ensure smooth behavior
clock = pygame.time.Clock()

# DELETE AFTER YOU UNDERSTAND HOW IT WORKS
# -----
# To create a circle, specify the color followed by the radius
circle = Circle("green", 50)
# To create a rectangle specify the color, width and height
rectangle = Rectangle("red", 100, 50)
# -----

# Some boolean expression for your while loop
game_over = False

# Game loop
while not game_over:
    # Handling events (i.e. what do you want to do when the user presses w)
    for event in pygame.event.get():
        # This is something you should ALWAYS have, that states if
        # the user presses the x on the window it should close
        if event.type == pygame.QUIT:
            game_over = True
    # DELETE THE CODE IN BETWEEN ---- AFTER YOU UNDERSTAND WHAT IT MEANS
    # Uncomment them to try them out
    # -----
    # You can update the position by the following!
    x_circle_pos, y_circle_pos = circle.get_position()
    x_rect_pos, y_rect_pos = rectangle.get_position()
    circle.set_position(x_circle_pos + 1, y_circle_pos + 1)
    rectangle.set_position(x_rect_pos + 1, y_rect_pos)
    
    # If you want to change the color
    # circle.set_color("red")
    # rectangle.set_color("blue")
    # Note how this all happens BEFORE we clear the screen, draw, and display to the screen.
    # If you want to change the size
    circle.set_radius(200)
    rectangle.set_size(100, 100)
    # -----


    # Clearing the screen
    screen.fill("black")

    # DELETE THE CODE IN BETWEEN ---- AFTER YOU UNDERSTAND WHAT IT MEANS
    # -----
    # To draw a circle
    screen.blit(circle.get_surface(), circle.get_position())
    # To draw a rectangle
    screen.blit(rectangle.get_surface(), rectangle.get_position())
    # -----

    # Displaying to the screen
    # Showing what you've drawn on the scren
    pygame.display.flip()

    # Setting framerate to 60FPS
    clock.tick(60)
pygame.quit() 