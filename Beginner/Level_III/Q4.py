class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

def main():
    # Taking input from the user
    length = float(input("Enter the length of the square: "))

    # Creating a Square object
    square = Square(length)

    # Displaying the area
    print(f"Area of the square: {square.area()}")

if __name__ == "__main__":
    main()