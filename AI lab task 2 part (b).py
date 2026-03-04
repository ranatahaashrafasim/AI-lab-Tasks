movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

n = int(input("How many movies you want to add: "))

for i in range(n):
    name = input("Movie name: ")
    budget = int(input("Budget: "))
    movies.append((name, budget))

total = 0
for movie in movies:
    total += movie[1]

average = total / len(movies)

print("Average Budget:", average)

count = 0

for movie in movies:
    if movie[1] > average:
        print(movie[0], "is higher than average by", movie[1] - average)
        count += 1

print("Movies above average:", count)