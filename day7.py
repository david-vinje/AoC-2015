lines = open("day7.txt").readlines()
d = dict()
for line in lines:
  line = line.split(" -> ")
  k = line[1].rstrip('\n')
  if "AND" in line[0]:
    line = line[0].split(" AND ")
    if not (k in d and line[0] in d and line[1] in d):
      continue
    a, b = [d[x] for x in line]
    d[k] = a & b
  elif "OR" in line[0]:
    line = line[0].split(" OR ")
    if not (k in d and line[0] in d and line[1] in d):
      continue
    a, b = [d[x] for x in line]
    d[k] = a | b
  elif "LSHIFT" in line[0]:
    line = line[0].split(" LSHIFT ")
    if not (k in d and line[1] in d):
      continue
    d[k] = d[line[0]] << int(line[1])
  elif "RSHIFT" in line[0]:
    line = line[0].split(" RSHIFT ")
    if not (k in d and line[0] in d):
      continue
    d[k] = d[line[0]] >> int(line[1])
  elif "NOT" in line[0]:
    line = line[0].split(" ")
    if not (k in d and line[1] in d):
      continue
    d[k] = ~int(d[line[1]]) & 0xFFFF
  else:
    d[k] = int(line[0])

print(~456)