friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend, enemy in zip(friends, enemies):
    if friend == "James":
        continue
    elif friend == enemy:
        print(f"{friend} we are not friends anymore")
    elif friend != enemy:
        print(f"{friend} we are the best friends")
