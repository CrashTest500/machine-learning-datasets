# This creates dummy weather data for each hour from beginning date to ending date
from datetime import date, timedelta
import random
import os

beginning_date = date(2020, 1, 1)
ending_date = date(2024, 1, 6)
date_diff = (ending_date - beginning_date).days
all_weather_options = ["sunny", "rainy", "cloudy", "snowy"]
winter_temperatures = list(range(51))
summer_temperatures = list(range(50, 101))
dataset = []

def get_random_weather(temp):
    allowed_weather = list(filter(lambda x: temp <= 32 or temp > 32 and x != 'snowy', all_weather_options))

    num = random.randrange(0, len(allowed_weather))
    return allowed_weather[num]

def get_random_temp(date: date):
    allowed_temps = summer_temperatures if date.month >= 5 and date.month <= 9 else winter_temperatures
    # print(f'{date} {allowed_temps}')
    num = random.randrange(0, len(allowed_temps))
    return allowed_temps[num]

def output_to_file():
    current_directory = os.getcwd()
    dest_folder = "data-files"
    full_path = os.path.join(current_directory, dest_folder)
    
    if os.path.exists(full_path) == False:
        os.mkdir(full_path)

    file = open("data-files\weather-data.csv", "w")
    for data in dataset:
        file.writelines(f'{data}\n')

    file.close()

def load_data():
    for i in range(date_diff):
        new_date = beginning_date + timedelta(days=i)
        for h in range(24):
            random_temp = get_random_temp(new_date)
            random_foreacst = get_random_weather(random_temp)
            
            hourly_forecast = f'{new_date} {h:02}:00,{random_foreacst},{random_temp}'
            dataset.append(hourly_forecast)

def main():
    load_data()
    output_to_file()

main()