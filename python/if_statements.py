opened_file = open('AppleStore.csv', encoding='utf8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
    
    # Complete code from here)
    
    
avg_rating_free_games  = sum(free_games_ratings) / len(free_games_ratings)

print(avg_rating_free_games)