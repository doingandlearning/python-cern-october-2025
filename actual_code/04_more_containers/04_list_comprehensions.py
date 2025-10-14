list_of_temperatures = [
    15, 14.9, 12, 17, 20, 26, 32
]

high_temperatures = []

for temperature in list_of_temperatures:
    if temperature > 20:
        high_temperatures.append(temperature)

print(high_temperatures)

low_temperatures = [t for t in list_of_temperatures if t < 20 ]
print(low_temperatures)
