def part_one():
  paper = 0
  for line in open('day2.txt', 'r'):
    l, w, h = [int(i) for i in line.split('x')]
    paper = paper + 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
  print(paper)
    
def part_two():
  ribbon = 0
  for line in open('day2.txt', 'r'):
    l = [int(i) for i in line.split('x')]
    ls = sorted(l)[:-1]
    ribbon = ribbon + ls[0]*2 + ls[1]*2 + l[0]*l[1]*l[2]
  print(ribbon)
  
# part_one()
part_two()