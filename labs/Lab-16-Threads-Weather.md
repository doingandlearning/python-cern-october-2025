# Lab 16: Multi-Threaded Weather Station Simulator

## Overview
In this lab, you'll build a simulated weather station that monitors multiple sensors concurrently using Python threading. This lab covers the same threading concepts as the original Lab 16, but with a more engaging real-world scenario.

## Background
Weather stations typically have multiple sensors (temperature, humidity, pressure, wind speed, etc.) that collect data at different intervals. In this simulation, each sensor will be represented by a separate thread that "reads" data at random intervals, simulating real-world sensor behavior.

## Part 1: Basic Weather Station

### Task 1.1: Understand the Sensor Reader Function
You've been provided with a starter template for the `sensor_reader()` function. Complete the implementation:

**Parameters:**
- `sensor_name` (string): The name of the sensor (e.g., "Temperature", "Humidity")
- `sensor_unit` (string): The unit of measurement (e.g., "°C", "%", "hPa")
- `max_interval` (int): Maximum time between readings in seconds
- `readings_count` (int): Number of readings to take (default: 10)

**Starter Code:**
```python
import threading
import time
import random

def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    """
    Simulates a weather sensor that takes readings at random intervals.
    Complete the implementation below.
    """
    for i in range(1, readings_count + 1):
        sleep_time = random.randint(1, max_interval)
        time.sleep(sleep_time)
        reading_value = random.randint(0, 100)
        print(f"[{sensor_name}] Reading #{i}: {reading_value} {sensor_unit}")
```

Example usage:
```python
sensor_reader("Temperature", "°C", 5, 10)
```

This creates a sensor called `Temperature` that will print 10 readings in celcius with a maximum delay between readings of 5 seconds.

### Task 1.2: Create Multiple Sensor Threads
Create and start threads for 5 different weather sensors:

1. **Temperature sensor** - reads every 1-3 seconds
2. **Humidity sensor** - reads every 2-5 seconds  
3. **Pressure sensor** - reads every 3-7 seconds
4. **Wind speed sensor** - reads every 1-4 seconds
5. **Rainfall sensor** - reads every 4-8 seconds

**Expected output example:**
```
[Temperature] Reading #1: 23 °C
[Wind Speed] Reading #1: 15 km/h
[Humidity] Reading #1: 67 %
[Temperature] Reading #2: 24 °C
[Pressure] Reading #1: 1013 hPa
[Rainfall] Reading #1: 2 mm
...
```

## Part 2: Advanced Features

### Task 2.1: Weather Alerts with Timer
Add a weather alert system that checks for extreme conditions every 10 seconds:

- Create a function `weather_alert()` that prints "⚠️  WEATHER ALERT: Checking conditions..." 
- Use a `Timer` to trigger this alert every 10 seconds
- The alert should run concurrently with your sensor readings

### Task 2.2: Continuous Monitoring
Modify your weather station to run continuously:

- Create a function `continuous_alert()` that:
  - Prints the alert message
  - Schedules the next alert using a new `Timer`
  - This creates a repeating alert system
- Run your weather station for 30 seconds total
- Use `time.sleep(30)` in your main function to keep it running

### Task 2.3: Data Logging
Add a simple data logging feature:

- Create a function `log_data()` that writes sensor readings to a file
- Modify your sensor readers to also log data to a file called `weather_log.txt`
- Each log entry should include timestamp, sensor name, and reading value

## Learning Objectives
By completing this lab, you will understand:

1. **Thread Creation and Management** - Creating multiple threads for concurrent execution
2. **Thread Arguments** - Passing parameters to thread functions
3. **Random Timing** - Using `random.randint()` and `sleep()` for realistic simulation
4. **Concurrent Output** - How multiple threads interact when printing to console
5. **Timer Usage** - Using `Timer` for delayed and repeating tasks

## Extension Ideas
- Add more sensor types (UV index, air quality, etc.)
- Implement a web dashboard using Flask
- Add data visualization with matplotlib
- Create a configuration file for sensor settings
- Implement sensor failure simulation
- Add data persistence with SQLite

## Sample Solution Structure
```python
import threading
import time
import random
from datetime import datetime

# Complete the sensor reader function (starter code provided)
def sensor_reader(sensor_name, sensor_unit, max_interval, readings_count=10):
    # TODO: Complete the implementation using the starter code provided
    pass

# Your alert functions
def weather_alert():
    # Implementation here
    pass

def continuous_alert():
    # Implementation here
    pass

# Main function
def main():
    # Create and start sensor threads
    # Set up timers
    # Run for specified duration
    pass

if __name__ == "__main__":
    main()
```

This lab provides the same fundamental threading concepts as the original but in a context that students can relate to and find more engaging!
