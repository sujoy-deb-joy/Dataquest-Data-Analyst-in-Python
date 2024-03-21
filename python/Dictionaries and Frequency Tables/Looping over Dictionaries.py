content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for content in content_ratings:
    content_ratings[content] /= total_number_of_apps
    content_ratings[content] *= 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']
