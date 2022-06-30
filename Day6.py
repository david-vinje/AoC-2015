import numpy as np
grid = np.zeros((1000,1000), dtype=int)
lines = open("day6.txt").readlines
for line in lines:
    input = line.split(" ")
    a, b = 1,3 if input[0] == "toggle" else 2,4
    x1, y1 = [int(x) for x in input[a].split(",")]
    x2, y2 = [int(x) for x in input[b].split(",")]
    if (input[0] == "toggle"):
        grid[x1:x2, y1:y2] = 0 if grid[x1:x2, y1:y2] else 1
    else:
        grid[x1:x2, y1:y2] = 1 if input[1] == "on" else 0