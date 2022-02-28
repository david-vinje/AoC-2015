def part1():
    f = open("day2.txt")
    lines = f.readlines()
    area = 0
    for line in lines:
        line = line.split("x")
        l, w, h = int(line[0]), int(line[1]), int(line[2])
        area += 2*l*w + 2*w*h + 2*h*l + min(l*w, min(w*h, l*h))
    print(area)

def part2():
    f = open("day2.txt")
    lines = f.readlines()
    area = 0
    for line in lines:
        line = line.split("x")
        dim = [int(line[0]), int(line[1]), int(line[2])]
        dim.sort()
        area += 2*dim[0]+2*dim[1]+dim[0]*dim[1]*dim[2]
    print(area)
part2() 
        