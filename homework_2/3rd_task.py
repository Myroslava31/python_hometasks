casino_blacklist = {'John Smith', 'Marta Smith', 'Ann Fox', 'Tom Thomas'}
poker_blacklist = {'Ann Fox', 'John Smith', 'Adam Fisher', 'Tom Thomas', 'Alice Cooper'}
alcohol_blacklist = {'Maria Fureiro', 'John Smith', 'Adam Fisher', 'Ann Fox'}
alco_casino_blacklist = alcohol_blacklist.intersection(casino_blacklist)
total_blacklist = alco_casino_blacklist.intersection(poker_blacklist)
print(total_blacklist)

