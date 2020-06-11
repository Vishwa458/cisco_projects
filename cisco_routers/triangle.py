from math import random
vertices = []
for i in range(3):                         # Do this 3 times
    x = random.randint(0, 500)             # Create a random x value
    y = random.randint(0, 500)             # Create a random y value
    vertices.append(graphics.Point(x, y))  # Add the (x, y) point to the vertices
triangle = graphics.Polygon(vertices)      # Create the triangle
triangle.setFill(colour)
triangle.draw(win)
