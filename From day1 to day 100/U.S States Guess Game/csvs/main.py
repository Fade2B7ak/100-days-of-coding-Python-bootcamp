import pandas
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#
# import csv

# with open('./weather_data.csv') as weather:
#     weathers = csv.reader(weather)
#     temps = []
#     for row in weathers:
#         if row[1] != 'temp':
#             temperat = int(row[1])
#             temps.append(temperat)

#
# data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
#
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# c_to_f = (int(monday_temp) * 9 / 5) + 32
# print(c_to_f)
#
# # dataframe from scratch
# data_dict = {
#     'students': ["Any", "James", "Dano"],
#     'scores': [76, 56, 65]
# }
# datata = pandas.DataFrame(data_dict)
# datata.to_csv('new_data.csv')
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])


data_dict = {
    'Colors': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')
