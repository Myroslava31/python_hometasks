import os
os.chdir("./directory/for/file")
with open ('text.txt', 'r') as file:
    result = file.read()
all_freq = {}
for i in result:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(str(all_freq))
