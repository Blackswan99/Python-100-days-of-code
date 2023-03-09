import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

temp_list = data.temp.to_list()
# Data in columns
print(data.temp.mean())
print(data.temp.max())
# Data in rows
max_celsius = data[data.temp == data.temp.max()].temp
max_fahrenheit = max_celsius * 1.8 + 32
print(max_fahrenheit)
