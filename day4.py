import hashlib
import re

key = "bgvyzdsv"
count = 0
while (not re.search('^00000', hashlib.md5((key+str(count)).encode('utf-8')).hexdigest())):
    count += 1   

print(count)

count = 0
while (not re.search('^000000', hashlib.md5((key+str(count)).encode('utf-8')).hexdigest())):
    count += 1   

print(count)