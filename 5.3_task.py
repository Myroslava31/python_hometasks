import os
import re

os.chdir("./directory/for/file")
with open ('text.txt', 'r') as file:
    result = file.read()
letters = re.findall(r'[A-z]', result)
letters_str = "".join(letters)
print(letters_str)
all_freq = {}
for letter in letters_str:
    if letter in all_freq:
        all_freq[letter] += 1
    else:
        all_freq[letter] = 1

print(str(all_freq))
