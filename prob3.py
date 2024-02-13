people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Use a lambda function as the sorting key
people.sort(key=lambda people: people [1])
print(people)
