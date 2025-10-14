# **Lab 05 Extra: Practice with Dictionaries, Sets, and List Comprehensions for Engineers and Scientists**

## **Objective**
This extra lab provides additional practice with dictionaries, sets, and list comprehensions using practical examples relevant to engineering and scientific work. You will reinforce your understanding of these important data structures without using functions.

You will:
1. **Work with dictionaries** to store and retrieve key-value pairs
2. **Use sets** to handle unique collections of data
3. **Practice list comprehensions** for creating lists efficiently
4. **Combine these concepts** in practical scientific scenarios

---

## **Tasks**

### **1. Experimental Data Logger**

Create a dictionary to store experimental measurements and work with it:

```python
# Sample data - sensor readings (sensor_id: temperature_celsius)
sensor_readings = {
    "Sensor_A": 23.5,
    "Sensor_B": 24.1,
    "Sensor_C": 22.8,
    "Sensor_D": 25.2,
    "Sensor_E": 23.9
}
```

**Tasks:**
- Print all sensor names
- Print all temperature readings
- Print Sensor_A's reading
- Add a new sensor "Sensor_F" with reading 24.7
- Update Sensor_B's reading to 25.1
- Remove Sensor_C from the readings
- Find the sensor with the highest temperature
- Find the sensor with the lowest temperature
- Calculate the average temperature
- Print sensors with readings above 24°C

---

### **2. Laboratory Inventory**

Create an inventory dictionary to track chemical supplies and quantities:

```python
# Start with an empty inventory
inventory = {}
```

**Tasks:**
- Add 500ml of hydrochloric acid to inventory
- Add 250g of sodium chloride to inventory
- Add 100ml of ethanol to inventory
- Add 50g of potassium hydroxide to inventory
- Print the entire inventory
- Print just the chemicals
- Print just the quantities
- Check if "hydrochloric acid" is in inventory
- Check if "sulfuric acid" is in inventory
- Update hydrochloric acid quantity to 750ml
- Remove sodium chloride from inventory
- Print the total number of different chemicals

---

### **3. Data Point Frequency Counter**

Count how many times each measurement value appears in experimental data:

```python
# Sample experimental measurements
measurements = [23.5, 24.1, 23.5, 25.2, 24.1, 23.5, 24.8, 25.2, 24.1]
```

**Tasks:**
- Create a dictionary to count measurement frequencies
- Print the frequency of each measurement value
- Find the most common measurement
- Find the least common measurement
- Print measurements that appear more than once
- Print measurements that appear exactly once

---

### **4. Research Team Operations**

Work with sets to find unique elements and relationships between research teams:

```python
# Sample data - researchers on different projects
physics_team = {"Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis", "Dr. Wilson"}
chemistry_team = {"Dr. Johnson", "Dr. Davis", "Dr. Miller", "Dr. Taylor", "Dr. Anderson"}
```

**Tasks:**
- Print all physics team members
- Print all chemistry team members
- Find researchers working on both projects
- Find researchers working only on physics
- Find researchers working only on chemistry
- Find all researchers (working on either project)
- Find researchers working on neither project (if we know all researchers)
- Check if "Dr. Smith" is on the physics team
- Check if "Dr. Miller" is on the physics team

---

### **5. Scientific Data Processing with List Comprehensions**

Create lists using list comprehensions for scientific data:

```python
# Sample data
temperatures = [20.5, 22.1, 18.7, 25.3, 19.8, 23.6, 21.2, 24.9, 17.4, 26.1]
elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
```

**Tasks:**
- Create a list of temperatures converted to Kelvin (K = C + 273.15)
- Create a list of even-indexed temperatures
- Create a list of odd-indexed temperatures
- Create a list of temperatures above 22°C
- Create a list of element name lengths
- Create a list of elements that start with 'H'
- Create a list of elements longer than 6 characters
- Create a list of tuples (element, length) for each element

---

### **6. Laboratory Equipment Database**

Create an equipment database using nested dictionaries:

```python
# Sample equipment database
equipment = {
    "Microscope_001": {"type": "Optical", "location": "Lab_A", "status": "Active"},
    "Centrifuge_002": {"type": "Centrifuge", "location": "Lab_B", "status": "Maintenance"},
    "Spectrometer_003": {"type": "Analytical", "location": "Lab_A", "status": "Active"}
}
```

**Tasks:**
- Print all equipment names
- Print Microscope_001's location
- Print Centrifuge_002's status
- Add new equipment "Balance_004" with type "Weighing", location "Lab_C", status "Active"
- Update Spectrometer_003's status to "Calibration"
- Remove Centrifuge_002 from equipment
- Print all equipment locations
- Print all equipment statuses
- Find equipment in Lab_A

---

### **7. Experimental Data Analysis with Sets and Dictionaries**

Analyze experimental results using both sets and dictionaries:

```python
# Sample experimental data
experiment_results = {
    "Trial_1": ["Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail"],
    "Trial_2": ["High", "Low", "High", "High", "Low", "High", "Low", "High"],
    "Trial_3": ["Red", "Blue", "Green", "Red", "Blue", "Red", "Green", "Blue"]
}
```

**Tasks:**
- Print all results for each trial
- Find unique results for each trial
- Count how many times "Pass" appears in Trial_1
- Count how many times "High" appears in Trial_2
- Find the most common result in Trial_3
- Find results that appear more than once in Trial_1
- Create a set of all unique results across all trials

---

### **8. Advanced List Comprehensions for Scientific Data**

Practice more complex list comprehensions with scientific data:

```python
# Sample data - experimental measurements
measurements = [
    ("Sensor_A", 23.5, "Temperature"),
    ("Sensor_B", 24.1, "Temperature"),
    ("Sensor_C", 78.2, "Humidity"),
    ("Sensor_D", 25.2, "Temperature"),
    ("Sensor_E", 82.1, "Humidity")
]
```

**Tasks:**
- Create a list of just the sensor names
- Create a list of just the values
- Create a list of names of temperature sensors
- Create a list of values from temperature sensors
- Create a list of tuples (name, value) for sensors with values above 24
- Create a list of names of humidity sensors with values above 80
- Create a dictionary from the list where sensor name is key and value is the measurement

---

## **Tips for Success**

- **Use `.keys()`** to get all keys from a dictionary
- **Use `.values()`** to get all values from a dictionary
- **Use `.items()`** to get both keys and values
- **Use `in`** to check if a key exists in a dictionary
- **Use `len()`** to get the number of items
- **Use `set()`** to create sets from lists
- **Use `list()`** to create lists from sets
- **Use `max()` and `min()`** to find highest/lowest values
- **Use `sum()`** to calculate totals

---

**Good luck and have fun practicing with dictionaries, sets, and list comprehensions in scientific contexts!**
