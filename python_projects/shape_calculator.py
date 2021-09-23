class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=%i, height=%i)" % (self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width**2) + (self.height**2))**0.5
        return diagonal

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            pic = ""
            for i in range(self.height):
                for j in range(self.width):
                    pic = pic + "*"
                pic = pic + "\n"
            return pic

    def get_amount_inside(self, shape):
        width = self.width
        height = self.height
        width_counter = 0
        height_counter = 0
        while width >= shape.width:
            width_counter = width_counter + 1
            width = width - shape.width
        while height >= shape.height:
            height_counter = height_counter + 1
            height = height - shape.height
        amount = width_counter * height_counter
        return amount


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=%i)" % (self.width)

    def set_side(self, side):
        self.width = side
        self.height = side




if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

