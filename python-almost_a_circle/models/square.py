#!/usr/bin/python3
"""
the class Square that inherits from Rectangle

In the path models/square.py

Class Square inherits from Rectangle

As you know, a Square is a special Rectangle,

so it makes sense this class Square inherits from Rectangle.

Now you have a Square class who has the same attributes and same methods.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle

    Class constructor: def __init__(self, size, x=0, y=0, id=None)

    You must not create new attributes for this class,

    use all attributes of Rectangle -

    As reminder: a Square is a Rectangle with the same width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height

        his super call will use the logic of the __init__ of the

        Rectangle class. The width and height must be assigned

        to the value of size.

        All width, height, x and y validation must inherit from Rectangle -

        same behavior in case of wrong data
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The overloading __str__ method should return

        [Square] (<id>) <x>/<y> - <size> -

        in our case, width or height
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
