from turtle import Turtle
# you can define STARTING_POSITION and forward as constant here to avoid touching main program body later
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):

        self.conjoin = []
        self.create_snake()
        self.head = self.conjoin[0]
        self.head.shapesize(3, 3)
        self.head.shape("classic")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("green")
        tim.penup()
        tim.goto(position)
        self.conjoin.append(tim)

    # to increase the shape of the snake
    def enlargement(self):
        self.add_segment(self.conjoin[-1].position())

    # to make every part of the snake to follow the head
    def move(self):
        """ """
        for t_conjoin in range(len(self.conjoin) - 1, 0, -1):
            xcor = self.conjoin[t_conjoin - 1].xcor()
            ycor = self.conjoin[t_conjoin - 1].ycor()
            self.conjoin[t_conjoin].goto(xcor, ycor)

        self.head.forward(15)

    def up(self):
        # the if statement was used so that the snake won't turn up directly while facing down
        if self.head.heading() != DOWN:
            self.head.setheading(0)
            self.head.left(UP)
        # OR SELF.HEAD.SETHEADING(UP)

    def right(self):
        # the if statement was used so that the snake won't turn right directly while facing left
        if self.head.heading() != LEFT:
            self.head.setheading(0)
            self.head.left(RIGHT)
        # OR SELF.HEAD.SETHEADING(RIGHT)

    def left(self):
        # the if statement was used so that the snake won't turn left directly while facing right
        if self.head.heading() != RIGHT:
            self.head.setheading(0)
            self.head.left(LEFT)
        # OR SELF.HEAD.SETHEADING(LEFT)

    def down(self):
        # the if statement was used so that the snake won't turn down directly while facing up
        if self.head.heading() != UP:
            self.head.setheading(0)
            self.head.left(DOWN)
        # OR SELF.HEAD.SETHEADING(DOWN)

    def reset(self):
        for snake in self.conjoin:
            snake.goto(1000, 1000)
        self.conjoin.clear()
        self.create_snake()
        self.head = self.conjoin[0]
        self.head.shapesize(3, 3)
        self.head.shape("classic")


