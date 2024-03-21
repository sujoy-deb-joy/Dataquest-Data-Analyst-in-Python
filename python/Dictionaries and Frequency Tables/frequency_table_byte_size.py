opened_file = open('../AppleStore.csv', encoding='utf8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for row in apps_data[1:]:
    size = float(row[2])
    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)
print(data_sizes)
