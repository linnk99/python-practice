
import turtle

def main():
    window = turtle.Screen()
    hector = turtle.Turtle()

    make_square(hector)

    turtle.mainloop()


def make_square(hector):
    length = int(input("Square size: "))

    for i in range(4):
        make_line_and_turn(hector, 100)


def make_line_and_turn(hector, length):
    hector.forward(length)
    hector.left(90)

if __name__ == '__main__':
    main()