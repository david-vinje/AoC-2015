def part1():
    f = open("day1.txt")
    line = f.readline()
    count = 0
    for i in line:
        if i == "(":
            count += 1
        else: 
            count -= 1
    print(count)

def part2():
    f = open("day1.txt")
    line = f.readline()
    count, val = 0, 0
    for c in line:
        if c == "(":
            val += 1
        else:
            val -= 1
        count += 1
        if val == -1:
            print(count)
            break
part2()