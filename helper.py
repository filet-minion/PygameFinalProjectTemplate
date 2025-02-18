import pygame

def check_if_colliding(object_one, object_two) -> bool:
    '''Checks if two objects are colliding using the bounding rectangles. Returns true if they are colliding. To use
    this simply pass the two items you want to check who are colliding. (e.g. check_if_colliding(circle_one, circle_two))'''
    obj_one_rect = object_one.get_surface().get_rect()
    obj_two_rect = object_two.get_surface().get_rect()
    obj_1_x, obj_1_y = object_one.get_position()
    obj_2_x, obj_2_y = object_two.get_position()
    obj_one_rect = obj_one_rect.move(obj_1_x ,obj_1_y)
    obj_two_rect = obj_two_rect.move(obj_2_x ,obj_2_y)
    return pygame.Rect.colliderect(obj_one_rect, obj_two_rect)