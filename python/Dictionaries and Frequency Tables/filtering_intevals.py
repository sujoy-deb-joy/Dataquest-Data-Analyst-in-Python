opened_file = open('../AppleStore.csv', encoding='utf8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

n_user_ratings = []
for row in apps_data[1:]:
    rating = int(row[5])
    n_user_ratings.append(rating)

ratings_max = max(n_user_ratings)
ratings_min = min(n_user_ratings)


user_ratings_freq = {'0 - 10000': 0, '10000 - 100000': 0, '100000 - 500000': 0, '500000 - 1000000': 0, '1000000+': 0}

for row in apps_data[1:]:
    user_ratings = int(row[5])

    if user_ratings <= 10000:
        user_ratings_freq['0 - 10000'] += 1

    elif 10000 < user_ratings <= 100000:
        user_ratings_freq['10000 - 100000'] += 1

    elif 100000 < user_ratings <= 500000:
        user_ratings_freq['100000 - 500000'] += 1

    elif 500000 < user_ratings <= 1000000:
        user_ratings_freq['500000 - 1000000'] += 1

    elif user_ratings > 1000000:
        user_ratings_freq['1000000+'] += 1


print(user_ratings_freq)
