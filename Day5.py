# At least three vowels
# At least one letter twice in a row
# Does not contain ab, cd, pq, or xy

vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]

def is_nice_part_1(input):
    count = 0
    for letter in input:
        if letter in vowels:
            count += 1
    if (count < 3):
        return 0

    for word in forbidden:
        if word in input:
            return 0
            
    for i in range(len(input)-1):
        if (input[i] == input[i+1]):
            return 1
    return 0

count = 0
f = open("day5.txt")
lines = f.readlines()
for line in lines:
    count += is_nice_part_1(line)
print(count)

def is_nice_part_2(input):
    nice = False
    for i in range(1, len(input)-1):
        if (input[i-1] == input[i+1]):
            nice = True
            break
    
    if (not nice):
        return 0
            
    for i in range(len(input)-1):
        s1 = input[i:i+2]
        for j in range(len(input)-1):
            s2 = input[j:j+2]
            if (i != j and i-1 != j and i+1 != j and s1 == s2):
                return 1
    return 0

count = 0
for line in lines:
    count += is_nice_part_2(line)
print(count)

