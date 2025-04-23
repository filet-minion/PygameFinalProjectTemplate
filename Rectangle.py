import pygame
# An abstraction to make a rectangle easier to draw
class Rectangle:
    def __init__(self, color, width, height, x_pos=0, y_pos=0):
        '''Creates the rectangle object, with the particular color, width, height, x position and y position.
        X position and y position are optional. If no x and y position are given it will default to
        0, 0.'''
        # Creating the surface to draw on
        self._surface = pygame.Surface((width, height))
        self._width = width
        self._height = height
        self._color = color

        self.x = x_pos
        self.y = y_pos
        self._update()
    # Getters
    def get_width(self):
        '''Returns the objects width as a float.'''
        return self. _width
    def get_height(self):
        '''Returns the objects height as a float.'''
        return self. _height
    
    def get_color(self):
        '''Returns the color of the rectangle'''
        return self._color
    
    def get_surface(self):
        '''Returns the drawable surface. Needed when calling screen.blit(...). 
        The way to use this is screen.blit(rect_variable_name.get_surface(), rect_variable_name.get_position())'''
        return self._surface

    def get_position(self):
        '''Returns the objects x and y coordinates in the form (x, y). To use this write a statement like:
        x, y = rect_variable_name.get_position()'''
        return (self.x, self.y)
    # Setters
    def set_position(self, x, y):
        '''Sets the objects position on the screen'''
        self.x = x
        self.y = y

    def set_width(self, width):
        '''Sets the width of the rectangle'''
        self._width = width
        self._surface = pygame.Surface((self._width, self._height))
        self._update()
    def set_height(self, height):
        '''Sets the height of the rectangle'''
        self._height = height
        self._surface = pygame.Surface((self._width, self._height))
        self._update()

    def set_size(self, width, height):
        '''Changes the size in the format width, height'''
        self.set_width(width)
        self.set_height(height)

    def set_color(self, color):
        '''Sets the color of the rectangle'''
        self._color = color
        self._surface.fill(color)
        self._update()

    def move(self, x_offset, y_offset):
        '''This takes the rectangles current location and shifts it by x_offset, y_offset. To use this
        simply do rectangle_variable_name.move(1, 1)'''
        self.x += x_offset
        self.y += y_offset
    
    def _update(self):
        self._surface.fill(self._color)