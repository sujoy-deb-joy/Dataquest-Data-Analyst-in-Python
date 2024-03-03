opened_file = open('AppleStore.csv', encoding='utf8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    name = row[1]
    apps_names.append(name)

print(apps_names[:5])    
# if else example
# fetch free apps_ratings

non_games_ratings = []

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    if genre != 'Games':
        non_games_ratings.append(rating)
    if price == 0.0:
        free_apps_ratings.append(rating)

avg_rating_free =  sum(free_apps_ratings ) / len(free_apps_ratings)
print("Average Rating of Free Apps: ", avg_rating_free)

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

print("Average Rating of Non Games: ", avg_rating_non_games)
    