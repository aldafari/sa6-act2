people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Use a lambda function as the sorting key
sorted_people = sorted(people, key=lambda x: people[1])
print(sorted_people)
