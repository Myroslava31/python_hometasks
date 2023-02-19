my_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odds = []
evens = []
for index, value in enumerate(my_elements):
    if (index % 2) == 0:
        evens.append((index, value))
    else:
        odds.append((index, value))
print(odds)
print(evens)
