import numpy as np
from scipy.signal import convolve2d

def power(x, y, s):
    return ((x + 10) * y + s) * (x + 10) // 100 % 10 - 5

dim1 = 300
grid = np.zeros((dim1, dim1), dtype=np.int64)

serial = 2866
for y in range(dim1):
    for x in range(dim1):
        # The puzzle uses 1-based indexing
        # Also for debug printing: y=rows, x=cols
        grid[y, x] = power(x + 1, y + 1, serial)

dim2 = 3  # start with 3x3 because that's part 1
curmax = absmax = 0

# Use clever condition for positive maximum
# because the trend is negative for larger squares (power is -5..+4)
while curmax >= 0 and dim2 <= dim1:
    # Convolution kernel all ones => sum of all the squares
    kernel = np.ones((dim2, dim2), dtype=np.int64)
    # mode='valid' means do not extend beyond dim1,
    # so the result of the convolution will be smaller by half dim2
    squares = convolve2d(grid, kernel, mode='valid')
    # Get the index of the maximum value
    my, mx = np.unravel_index(squares.argmax(), squares.shape)
    # The maximum value itself for this dim2
    curmax = squares[my, mx]
    if curmax > absmax:
        absmax = curmax
        # Plus 1 because puzzle uses 1-based indexing
        print("%d,%d,%d" % (mx + 1, my + 1, dim2))
    dim2 += 1
