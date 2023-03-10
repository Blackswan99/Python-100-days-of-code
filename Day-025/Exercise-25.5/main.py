data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
#print(fur_color.value_counts())
fur_color_dataframe = pandas.DataFrame(fur_color.value_counts())
print(fur_color_dataframe)
