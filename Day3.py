def part1():
    f = open("day3.txt")
    x, y = 0, 0
    pos = set()
    pos.add((x, y))
    line = f.readline()
    for char in line:
        if char == "<":
            x -= 1
        elif char == ">":
            x += 1
        elif char == "^":
            y += 1
        else:
            y -= 1
        pos.add((x, y))
    print(len(pos))

def part2():
    f = open("day3.txt")
    line = f.readline()
    x1, y1, x2, y2 = 0, 0, 0, 0
    pos = set()
    pos.add((x1,y1))
    for idx in range(0, len(line), 2):
        if line[idx] == "<":
            x1 -= 1
        elif line[idx] == ">":
            x1 += 1
        elif line[idx] == "^":
            y1 += 1
        else: 
            y1 -= 1
        pos.add((x1,y1))    
        
        if line[idx+1] == "<":
            x2 -= 1
        elif line[idx+1] == ">":
            x2 += 1
        elif line[idx+1] == "^":
            y2 += 1
        else: 
            y2 -= 1
        pos.add((x2,y2))
    print(len(pos))
part2()
    