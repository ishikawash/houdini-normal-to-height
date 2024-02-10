from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plot

Size = namedtuple("Size", "x y")

def main():
    grid_size = 32
    size = Size(grid_size, grid_size)
    n = size.x * size.y
    A = np.zeros((n, n))

    for y in range(size.y):
        for x in range(size.x):
            i = y*size.x + x
            A[i, i] = 4
            if x > 0:
                A[i - 1, i] = -1
            if x < size.x - 1:
                A[i + 1, i] = -1
            if y > 0:
                A[i, i - size.x] = -1
            if y < size.y - 1:
                A[i, i + size.x] = -1

    plot.imshow(A, cmap="binary")
    plot.colorbar()
    plot.show()

main()
