import pandas

# data = pandas.read_csv("D:\\Projects\\py-100-days\\Day25\\weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# print(data["temp"].max())

# monday = data[data.day == "Monday"]
# print(monday.temp[0])



data = pandas.read_csv("D:\\Projects\\py-100-days\\Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])

cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

black_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_count, cinnamon_count, black_count)
data_dict= {
    "color" : ['Gray', 'Cinnamon', 'Black'],
    "count" : [gray_count, cinnamon_count, black_count]
}

df =pandas.DataFrame(data_dict)
df.to_csv("Day25/fur-squirrel-count.csv")