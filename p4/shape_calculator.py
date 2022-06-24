class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return  (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        res = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        for lv in range(self.height):
            res += "*" * self.width + "\n"
        
        return res 

    def get_amount_inside(self, other_shape):
        return (self.width // other_shape.width) * (self.height // other_shape.height)



class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.height})"
 
    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side
    
    def set_width(self, side_width):
            self.width = side_width
            self.height = side_width

    def set_height(self, side_height):
            self.height = side_height
            self.width = side_height
