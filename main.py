# with open("./weather-data.csv") as file:
#     data = file.readlines()
#     print(data)
# from csv import reader
#
# with open("./weather-data.csv") as data_file:
#     weather_data = reader(data_file)
#     temperatures = []
#     for temp in weather_data:
#         if temp[1] != "temp":
#             temperatures.append(int(temp[1]))
#     print(temperatures)

import pandas

# csv_data = pandas.read_csv("./weather-data.csv")
# print(csv_data)
# print(csv_data["temp"])
# print(type(csv_data))
# print(type(csv_data["temp"]))

# data_dict = csv_data.to_dict()
# print(data_dict)
# data_list = csv_data["temp"].to_list()
# print(data_list)
# print(len(data_list))

# sum = 0
# for temp in data_list:
#     sum += temp
# average = sum / len(data_list)
# print(average)
# # or
# average = sum(data_list) / len(data_list)
# print(average)
# # or
# print(csv_data["temp"].mean())
# print(csv_data["temp"].max())

# # Get data in Columns
# # Treat like a Dictionary
# print(csv_data['day'])
# print(csv_data['temp'])
# print(csv_data['condition'])
# # Treat like an Object
# print(csv_data.day)
# print(csv_data.temp)
# print(csv_data.condition)

# # Get data in Row
# print(csv_data[csv_data.day == "Monday"])
# print(csv_data[csv_data.temp == csv_data["temp"].max()])
# sunday = csv_data[csv_data.day == "Sunday"]
# print(sunday.condition)
#
# monday = csv_data[csv_data.day == "Monday"]
# temp = monday.temp * 9/5 + 32
# print(temp)

# # Create a Dataframe from Scratch
# data_dict = {
#     "students": ["Amy", "Jack", "John"],
#     "scores": [34, 56, 87],
# }
#
# new_csv_file = pandas.DataFrame(data_dict)
# print(new_csv_file)
# new_csv_file.to_csv("new_csv.csv")

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
colors = ["Gray", "Cinnamon", "Black"]
count = []
for color in colors:
    color = data[data["Primary Fur Color"] == color]["Primary Fur Color"].count()
    count.append(color)

data_dict = {
    "Fur Color": colors,
    "Count": count,
}

df = pandas.DataFrame(data_dict).to_csv("Squirrel.csv")
