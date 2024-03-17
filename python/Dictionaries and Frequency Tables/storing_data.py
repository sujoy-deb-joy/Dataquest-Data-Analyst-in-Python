opened_file = open('../AppleStore.csv', encoding='utf8')
from csv import reader

read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]
content_rating_numbers = [['4+', '9+', '12+', '17+'], [4433, 987, 1155, 622]]
content_ratings_dict = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
