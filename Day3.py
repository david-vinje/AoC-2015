def part_one():
  f = open('day3.txt', 'r')
  x, y = 0, 0
  houses = {(0,0)}
  for i in list(f.readline()):
    if i == '>':
      x = x+1
    elif i == '<':
      x = x-1
    elif i == '^':
      y = y-1
    else:
      y = y+1
    houses.add((x,y))
  print(len(houses))
    
def part_two():
  f = open('day3.txt', 'r')
  x1, y1, x2, y2 = 0, 0, 0, 0
  houses = {(0,0)}
  turn = 0
  for i in list(f.readline()):
    if turn % 2 == 0:
      if i == '>':
        x1 = x1+1
      elif i == '<':
        x1 = x1-1
      elif i == '^':
        y1 = y1-1
      else:
        y1 = y1+1
      houses.add((x1,y1))
    else:
      if i == '>':
        x2 = x2+1
      elif i == '<':
        x2 = x2-1
      elif i == '^':
        y2 = y2-1
      else:
        y2 = y2+1
      houses.add((x2,y2))
    turn = turn+1
      
  print(len(houses))
  
# part_one()
part_two()