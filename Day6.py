import numpy as np
n = 1000
grid = np.zeros((n, n), dtype=int)
lines = open("day6.txt").readlines()

def part_two():
    for line in lines:
        line = line.split(" ")
        if line[0] == "turn":
            x1, y1 = [int(x) for x in line[2].split(",")]
            x2, y2 = [int(x) for x in line[4].split(",")]
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = grid[i][j]+1 if line[1] == "on" else max(0, grid[i][j]-1)
        else:
            x1, y1 = [int(x) for x in line[1].split(",")]
            x2, y2 = [int(x) for x in line[3].split(",")]
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] += 2
    print(np.sum(grid))
part_two()

def part_one():
    for line in lines:
        line = line.split(" ")
        if line[0] == "turn":
            x1, y1 = [int(x) for x in line[2].split(",")]
            x2, y2 = [int(x) for x in line[4].split(",")]
            toggle = 1 if line[1] == "on" else 0
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = toggle
        else:
            x1, y1 = [int(x) for x in line[1].split(",")]
            x2, y2 = [int(x) for x in line[3].split(",")]
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    grid[i][j] = 0 if grid[i, j] else 1
    print(np.sum(grid))