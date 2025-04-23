import pygame
# An abstraction to make text easier to use
class Text:
    def __init__(self, font_path, font_size, font_color="white", str_to_render = "", x_pos=0, y_pos=0):
        '''Creates a text object with the desired font, font size, font color,
        and string to render, x position and y position. If no x and y position are given ite will default to
          0, 0  '''
        self._font = pygame.font.Font(font_path, font_size)
        self._color = font_color
        self._text = str_to_render
        self.x = 0
        self.y = 0
        self._update()

    # Getters
    def get_width(self):
        '''Returns the width of the bounding box of the text as a float. '''
        return self._surface.get_rect().width
    
    def get_height(self):
        '''Returns the height of the bounding box of the text as a float. '''
        return self._surface.get_rect().height
    
    def get_surface(self):
        '''Returns the drawable surface. Needed when calling screen.blit(...).
        The way to use this is screen.blit(text_variable_name.get_surface(), text_variable_name.get_position())'''
        return self._surface
    
    def get_position(self):
        '''Returns the x and y coordinates in the form (x, y). To use this write a statement like:
        x, y = text_variable_name.get_position()'''
        return (self.x, self.y)
    
    def get_text(self):
        '''Returns the current text'''
        return self._text
    
    def get_color(self):
        '''Returns the color of the text'''
        return self._color 

    # Setters
    def set_text(self, string_to_render):
        '''Sets the text to render of the text item'''
        self._text = string_to_render
        self._update()
    
    def set_color(self, color):
        '''Sets the color of the text'''
        self._color = color
        self._update()

    def set_position(self, x_pos, y_pos):
        '''Sets the objects position on the object'''
        self.x = x_pos
        self.y = y_pos

    def move(self, x_offset, y_offset):
        '''This takes the texts current location nand shifts it by x_offset, y_offset. 
        To use this simply do text_variable_name.move(1, 1)'''
        self.x += x_offset
        self.y += y_offset
    
    def _update(self):
        self._surface = self._font.render(self._text, True, self._color)

