import pygame
# An abstraction to make a rectangle easier to draw
pygame.init()

class SimpleSprite:
    def __init__(self, img_path, width, height, x_pos = 0, y_pos = 0):
        '''Creates a sprite object with the corresponding image, of specified width, height,
        x position and y position. If no x position and y position are specified it will default to 0, 0'''
        self._image = pygame.image.load(img_path).convert_alpha()
        self._width = width
        self._height = height
        self._update()
        self.x = x_pos
        self.y = y_pos
    # Getters
    def get_width(self):
        '''Returns the objects width as a float.'''
        return self. _width

    def get_height(self):
        '''Returns the objects height as a float.'''
        return self. _height
    def get_surface(self):
        '''Returns the drawable surface. Needed when calling screen.blit(...). 
        The way to use this is screen.blit(sprite_variable_name.get_surface(), sprite_variable_name.get_position())'''
        return self._surface

    def get_position(self):
        '''Returns the objects x and y coordinates in the form (x, y). To use this write a statement like:
        x, y = sprite_variable_name.get_position()'''
        return (self.x, self.y)

    # Setters
    def set_position(self, x, y):
        '''Sets the objects position on the screen'''
        self.x = x
        self.y = y

    def set_width(self, width):
        '''Sets the width of the sprite'''
        self._width = width
        self._update()

    def set_height(self, height):
        '''Sets the height of the sprite'''
        self._height = height
        self._surface = pygame.Surface((self._width, self._height))
        self._update()

    def set_size(self, width, height):
        '''Changes the size in the format width, height'''
        self.set_width(width)
        self.set_height(height)

    def _update(self):
        self._surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
        pygame.transform.scale(self._image, (self._width, self._height), self._surface)
        self._surface = self._surface.convert_alpha()


