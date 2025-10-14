import statistics


def add(a, b):
    return a + b

print(add(1,2))
print(add("1", "2"))

import statistics

def stats_of_numbers(list_of_numbers):
    minimum = min(list_of_numbers)
    maximum = max(list_of_numbers)
    mean = sum(list_of_numbers) / len(list_of_numbers)
    mode = statistics.mode(list_of_numbers)

    return {"min": minimum, "max":maximum, "mean": mean, "mode":mode}

print(stats_of_numbers([1,2,3,4,5,5]))

mode = stats_of_numbers([1,2,3,4,5,5])["mode"]
print(mode)