import numpy as np
# from scipy.

def power(x, y, s):
    return ((x + 10) * y + s) * (x + 10) // 100 % 10 - 5

# print(power(  3,   5,  8))
# print(power(122,  79, 57))
# print(power(217, 196, 39))
# print(power(101, 153, 71))

dim = 300
grid = np.zeros((dim, dim), dtype=np.int8)

# serial = 18
# for y in range(dim):
#     for x in range(dim):
#         grid[y, x] = power(x + 1, y + 1, serial)

# print(grid[43:48, 31:36])

# serial = 42
# for y in range(dim):
#     for x in range(dim):
#         grid[y, x] = power(x + 1, y + 1, serial)

# print(grid[59:64, 19:24])

serial = 2866
for y in range(dim):
    for x in range(dim):
        grid[y, x] = power(x + 1, y + 1, serial)

kernel = np.ones((3, 3), dtype=np.int8)
