# This creates dummy weather data for each hour from beginning date to ending date
from datetime import date, timedelta
import random
import os

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

    print(f'{len(dataset)} record(s) written to file')

def load_data():
    for i in range(date_diff):
        new_date = beginning_date + timedelta(days=i)
        for h in range(24):
            random_temp = get_random_temp(new_date)
            random_foreacst = get_random_weather(random_temp)
            
            hourly_forecast = f'{new_date} {h:02}:00,{random_foreacst},{random_temp}'
            dataset.append(hourly_forecast)

def gather_inputs():
    is_valid = False
    beginning_date_local = date(1900, 1, 1)
    ending_date_local = date(1900, 1, 1)

    while is_valid == False:
        print("Enter beginning date: yyyy-mm-dd")
        beginning_date_input = input()
        try:
            beginning_date_local = date.fromisoformat(beginning_date_input)
            is_valid = True
        except:
            print("invalid, try again!!!")

    is_valid = False

    while is_valid == False:
        print ("Enter ending date: yyyy-mm-dd")
        ending_date_input = input()
        
        try:
            ending_date_local = date.fromisoformat(ending_date_input)
            is_valid = True
        except:
            print("invalid, try again!!!")

    return beginning_date_local, ending_date_local

def main():
    load_data()
    output_to_file()

beginning_date, ending_date = gather_inputs()
date_diff = (ending_date - beginning_date).days

main()