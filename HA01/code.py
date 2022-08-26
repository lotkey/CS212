"""
This program draws 5 non-overlapping squares of random sizes and fills them in with random colors.
"""

import turtle  # for graphics
import random  # for random.random
import sys  # for sys.exit


def main() -> int:
    turtle.shape(name="turtle")
    turtle.speed("fast")
    square.draw_squares(5)
    turtle.done()  # had to add this line so the turtle window wouldn't automatically close in VS code
    return 1  # successful exit code


class square:
    """
    Represents a square on a turtle screen
    """

    def draw_squares(count: int) -> None:
        """
        ### Params:
        - count: int
          - Number of squares to draw on the turtle screen
        """

        prev_pos = (
            turtle.pos()
        )  # store the turtle's previous position so it can be moved back to there
        squares = []  # store all the drawn squares to avoid overlapping

        # brute-force method for avoiding overlapping squares
        # This is not the optimal way to do this, but it works fine
        #   for a few squares on a big canvas.
        while len(squares) < count:
            location = (
                random.randint(-400, 400),
                random.randint(-400, 400),
            )  # generate a random location in ([-400, 400), [-400, 400))
            side_length = random.randint(
                30, 100
            )  # generate a random square side length in [30, 100)
            s = square(location, side_length)

            overlaps = False
            for drawn_square in squares:
                if drawn_square.overlaps(s):
                    overlaps = True
                    break

            # if the squares do not overlap: draw the new square and add it to the list
            # else: back to the beginning of the while loop
            if not overlaps:
                s.draw()
                squares.append(s)

        turtle_teleport(prev_pos)  # move the turtle back to where it was originally

    def __init__(self, location: "tuple[float, float]", side_length: float):
        """
        ### Params:
        - location: tuple[float, float]
          - location of upper-left corner of the square on the turtle screen
        - side_length: float
          - length of the sides of the square
        """

        self.location = location
        self.side_length = side_length

    def left(self) -> float:
        """
        ### Returns:
        - The x coordinate of the left side of the square
        """

        return self.location[0]

    def right(self) -> float:
        """
        ### Returns:
        - The x coordinate of the right side of the square
        """

        return self.location[0] + self.side_length

    def top(self) -> float:
        """
        ### Returns:
        - The y coordinate of the top side of the square
        """

        return self.location[1] + self.side_length

    def bottom(self) -> float:
        """
        ### Returns:
        - The y coordinate of the bottom side of the square
        """

        return self.location[1]

    def overlaps(self, other: "type[square]") -> bool:
        """
        ### Params:
        - other: square
          - The square to test overlapping with
        ### Returns:
        - True if the squares overlap
        """

        # Skip the below comparisons to save on execution time
        if self.location == other.location:
            return True

        return (
            self.left() < other.right()
            and self.right() > other.left()
            and self.top() > other.bottom()
            and self.bottom() < other.top()
        )

    def draw(self):
        """
        Draws the square and fills it with a random color
        """

        turtle_teleport(self.location)  # teleport to the square's location
        fillcolor = (
            random.random(),
            random.random(),
            random.random(),
        )  # generate a random fill color of ([0-1), [0-1), [0-1))
        turtle.fillcolor(fillcolor)  # set the fill color
        turtle.begin_fill()  # start filling
        turtle.width(self.side_length / 20)  # set the line width for aesthetics

        # draw all four sides
        for _ in range(4):
            turtle.forward(self.side_length)
            turtle.left(90)

        turtle.end_fill()  # stop filling the square


def turtle_teleport(location: "tuple[float, float]") -> None:
    """
    Move the turtle to another location without drawing

    ### Params:
    - location: tuple[float, float]
      - Location to teleport the turtle to
    """

    turtle.penup()  # Pick the pen up to stop drawing
    turtle.goto(location)  # Move the turtle
    turtle.pendown()  # Put the pen back down to continue drawing


# With this at the bottom, everything is defined before main is called
# This improves readability because all the implementation details can be put after main is defined
if __name__ == "__main__":
    sys.exit(main())
