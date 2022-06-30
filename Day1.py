def part_one():
  floor = 0
  f = open("day1.txt", "r")
  for i in list(f.readline()):
    if i == '(': 
      floor = floor+1
    else:
      floor = floor-1
  print(floor)

def part_two():
  count, floor = 0, 0
  f = open("day1.txt", "r")
  for i in list(f.readline()):
    count = count+1
    if i == '(': 
      floor = floor+1
    else:
      floor = floor-1
    if floor == -1:
      print(count)
      break
      
part_one()
part_two()