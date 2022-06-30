def part_one():
  f = open('day5.txt', 'r')
  vowels = 'aeiou'
  forbidden = ['ab', 'cd', 'pq', 'xy']
  nice_count = 0
  for line in f:
    # condition 1
    vowel_count = 0
    for i in line:
      if i in vowels:
        vowel_count = vowel_count+1
    if vowel_count < 3:
      continue
    
    # condition 2
    is_nice = False
    for j in range(len(line)-1):
      if line[j] == line[j+1]:
        is_nice = True
        break
    if not is_nice:
      continue
    
    # condition 3
    for j in range(len(line)-1):
      if line[j]+line[j+1] in forbidden:
        is_nice = False
        break
    if is_nice:
      nice_count = nice_count+1
      
  print(nice_count)
    
def part_two():
  count = 0
  f = open('day5.txt', 'r')
  nice_count = 0
  for line in f:
    count += 1
    # condition 1
    is_nice = False
    for i, _ in enumerate(line):
      letters = line[i:i+2]
      substring = line[i+2:]
      if letters in substring:
        is_nice = True
        break
    if not is_nice:
      continue
    
    # condition 2
    for i in range(len(line)-2):
      first_letter = line[i]
      second_letter = line[i+2]
      if line[i] == line[i+2]:
        nice_count += 1
        break
  print(nice_count)
  
part_one()
part_two()