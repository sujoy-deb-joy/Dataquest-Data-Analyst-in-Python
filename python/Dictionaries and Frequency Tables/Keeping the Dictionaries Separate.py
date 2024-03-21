content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions = {}
c_ratings_percentages = {}

for content in content_ratings:
    proportion = (content_ratings[content] / total_number_of_apps)
    c_ratings_proportions[content] = proportion
    c_ratings_percentages[content] = proportion * 100


