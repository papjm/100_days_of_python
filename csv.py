#working with csv files(comma separated values:)
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
