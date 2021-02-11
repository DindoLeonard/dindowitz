import turtle as t
screen = t.Screen()

# This is the class for snake


class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]

    def create_snake(self):
        position = 0
        for _ in range(0, 2):
            piece = t.Turtle("square")
            piece.color("white")
            piece.penup()
            piece.setx(position)
            position -= 20
            self.pieces.append(piece)

    def move(self):
        for piece in range(len(self.pieces)-1, 0, -1):
            x = self.pieces[piece-1].xcor()
            y = self.pieces[piece-1].ycor()
            self.pieces[piece].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_piece(self):
        piece = t.Turtle()
        piece.shape("square")
        piece.color("white")
        piece.penup()
        self.pieces.append(piece)
        x = self.pieces[-2].xcor()
        y = self.pieces[-2].ycor()
        piece.goto(x=x, y=y)

    def reset(self):
        for piece in self.pieces:
            piece.goto(1000, 1000)
        self.pieces.clear()
        self.create_snake()
        self.head = self.pieces[0]


