opened_file = open('AppleStore.csv', encoding='utf8')
from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])

    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)

avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Not-free apps (average)

Not_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])

    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        Not_free_games_social_ratings.append(rating)

avg_not_free = sum(Not_free_games_social_ratings) / len(Not_free_games_social_ratings)
print(avg_not_free)
