# SFML-Inspired OOP Pygame Abstraction

## Purpose

The purpose of this project is to allow for introductory python students to create pygame projects with very little pygame overhead. Through these files, I teach my students the basics of pygame (i.e. basic event handling, simple windows, blitting etc.). I also utilize this to teach basics of game programming without needing to worry about learning pygame.

This project is inspired heavily by the C++ SFML libary and uses very similar syntax to the sfml library.

## Overview
Each file is self contained, meaning each student only needs to include the file they need to use for their project. I simply have my students follow the convention:

```py
from CLASS_NAME import CLASS_NAME
```

which minimizes the need to remember what is included in each file. The only exception is the helper file where it contains a simple collision detection for these shapes. Every file also has docstrings denoting what each method does.

## Dependencies
This project was written using pygame 2.6.1.

## Important Notes:
<ol>
    <li>
        Taking a look at the class files appears to have plenty of code duplication. That is intentional as I do not want to obfuscate the implementation with complicated abstractions. Although an interface could be created to minimize code duplication, I deliberately did not implement them as it would "black box" the classes for my students for when they become familiar with classes. 
    </li>
    <li>
        This project is simply instructional and is not meant to be efficient in any way. Often times, students have some mathematical background and are familiar with x, y coordinate systems. Instead of having my students utilize a bunch of variables (where lists may have not yet been taught yet), I let them focus on the programming logic. It is meant to be a project to get students familiar with the concepts and inspire them to want to pursure programming in the future.
    </li>
</ol>