import csv

integer_list = []
with open("weather-data.csv") as data_file:
    data = data_file.readlines()
    

with open('weather-data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for item in row:
            try:
                integer_list.append(int(item))
            except ValueError:
                pass
print(integer_list)
