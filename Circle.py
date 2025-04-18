import pygame
# An abstraction to make a circle easier to draw

class Circle:
    def __init__(self, color, radius, x_pos=0, y_pos=0):
        # Creating the surface to draw on
        self._surface = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        self._surface = self._surface.convert_alpha()
        # Saving the radius
        self._radius = radius
        # Saving the color
        self._color = color
        # Saving coordinates
        self.x = x_pos
        self.y = y_pos
        self._update()
    # Getters
    def get_radius(self):
        '''Returns the objects radius as a float.'''
        return self. _radius
    
    def get_color(self):
        '''Returns the color of the circle'''
        return self._color
    
    def get_surface(self):
        '''Returns the drawable surface. Needed when calling screen.blit(...). 
        The way to use this is screen.blit(circle_variable_name.get_surface(), circle_variable_name.get_position())'''
        return self._surface

    def get_position(self):
        '''Returns the objects x and y coordinates in the form (x, y). To use this write a statement like:
        x, y = circle_variable_name.get_position()'''
        return (self.x, self.y)
    # Setters
    def set_position(self, x, y):
        '''Sets the objects position on the screen'''
        self.x = x
        self.y = y

    def set_radius(self, radius):
        '''Sets the radius of the circle'''
        self._radius = radius
        self._update()

    def set_color(self, color):
        '''Sets the color of the circle'''
        self._color = color
        self._update()

    
    def _update(self):
        self._surface = pygame.Surface((2 * self._radius, 2 * self._radius), pygame.SRCALPHA)
        self._surface = self._surface.convert_alpha()
        pygame.draw.circle(self._surface, self._color, (self._radius, self._radius), self._radius)