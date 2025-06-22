
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


movies_with_avg = []

for title, year, ratings in movies:
    average = round(sum(ratings) / len(ratings), 2)
    if average >= 6:
        movies_with_avg.append((title, year, average))


    
sorted_list = sorted(movies_with_avg, key=lambda x: x[2], reverse=True) # sort the list based on average and sort it descending order

for title, year, average in sorted_list:
    print(f"{title} ({year}) - Average rating: {average}")












