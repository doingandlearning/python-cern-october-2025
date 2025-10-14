# **Lab 06 Extra: Practice with Functions for Engineers and Scientists**

## **Objective**
This extra lab provides additional practice with functions using practical examples relevant to engineering and scientific work. You will reinforce your understanding of function definition, parameters, return values, and scope.

You will:
1. **Create functions** for common scientific calculations
2. **Use parameters** to make functions flexible and reusable
3. **Return values** from functions for data processing
4. **Combine functions** to solve complex problems
5. **Practice good function design** with clear names and purposes

---

## **Tasks**

### **1. Temperature Conversion Functions**

Create functions to convert between different temperature scales:

**Tasks:**
- Create a function `celsius_to_fahrenheit(celsius)` that converts Celsius to Fahrenheit
- Create a function `fahrenheit_to_celsius(fahrenheit)` that converts Fahrenheit to Celsius
- Create a function `celsius_to_kelvin(celsius)` that converts Celsius to Kelvin
- Test your functions with sample temperatures: 0°C, 25°C, 100°C
- Create a function `convert_temperature(temp, from_scale, to_scale)` that converts between any two scales

**Formulas:**
- F = (C × 9/5) + 32
- C = (F - 32) × 5/9
- K = C + 273.15

---

### **2. Scientific Calculator Functions**

Create a collection of basic scientific calculation functions:

**Tasks:**
- Create a function `calculate_area_circle(radius)` that returns the area of a circle
- Create a function `calculate_volume_sphere(radius)` that returns the volume of a sphere
- Create a function `calculate_density(mass, volume)` that returns density
- Create a function `calculate_pressure(force, area)` that returns pressure
- Create a function `calculate_kinetic_energy(mass, velocity)` that returns kinetic energy
- Test all functions with sample values

**Formulas:**
- Area of circle: A = π × r²
- Volume of sphere: V = (4/3) × π × r³
- Density: ρ = m/V
- Pressure: P = F/A
- Kinetic energy: KE = (1/2) × m × v²

---

### **3. Data Analysis Functions**

Create functions to analyze experimental data:

**Tasks:**
- Create a function `calculate_average(numbers)` that returns the average of a list of numbers
- Create a function `find_maximum(numbers)` that returns the maximum value in a list
- Create a function `find_minimum(numbers)` that returns the minimum value in a list
- Create a function `calculate_range(numbers)` that returns the range (max - min)
- Create a function `count_above_threshold(numbers, threshold)` that counts values above a threshold
- Test with sample data: [23.5, 24.1, 22.8, 25.2, 23.9, 24.7, 22.1, 25.8]

---

### **4. Unit Conversion Functions**

Create functions for common unit conversions in science and engineering:

**Tasks:**
- Create a function `meters_to_feet(meters)` that converts meters to feet
- Create a function `feet_to_meters(feet)` that converts feet to meters
- Create a function `kilograms_to_pounds(kg)` that converts kilograms to pounds
- Create a function `pounds_to_kilograms(lbs)` that converts pounds to kilograms
- Create a function `liters_to_gallons(liters)` that converts liters to gallons
- Test all functions with sample values

**Conversion Factors:**
- 1 meter = 3.28084 feet
- 1 kilogram = 2.20462 pounds
- 1 liter = 0.264172 gallons

---

### **5. Chemical Formula Functions**

Create functions for basic chemistry calculations:

**Tasks:**
- Create a function `calculate_molar_mass(atomic_masses)` that takes a list of atomic masses and returns total molar mass
- Create a function `calculate_moles(mass, molar_mass)` that calculates number of moles
- Create a function `calculate_concentration(moles, volume)` that calculates molarity
- Create a function `calculate_ph(hydrogen_ion_concentration)` that calculates pH
- Test with sample data: atomic masses [12.01, 1.01, 16.00] for CO₂

**Formulas:**
- Molar mass = sum of atomic masses
- Moles = mass / molar mass
- Molarity = moles / volume (in liters)
- pH = -log₁₀[H⁺]

---

### **6. Statistical Analysis Functions**

Create functions for basic statistical analysis:

**Tasks:**
- Create a function `calculate_mean(numbers)` that returns the mean
- Create a function `calculate_median(numbers)` that returns the median
- Create a function `calculate_standard_deviation(numbers)` that returns the standard deviation
- Create a function `calculate_variance(numbers)` that returns the variance
- Create a function `find_outliers(numbers, threshold)` that finds values more than threshold standard deviations from mean
- Test with sample data: [12.3, 15.7, 18.2, 14.1, 16.8, 13.9, 17.4, 15.2, 19.1, 14.6]

---

### **7. Engineering Design Functions**

Create functions for basic engineering calculations:

**Tasks:**
- Create a function `calculate_stress(force, area)` that calculates stress
- Create a function `calculate_strain(original_length, change_in_length)` that calculates strain
- Create a function `calculate_youngs_modulus(stress, strain)` that calculates Young's modulus
- Create a function `calculate_heat_transfer(area, temperature_diff, time, thermal_conductivity)` that calculates heat transfer
- Create a function `calculate_efficiency(useful_output, total_input)` that calculates efficiency percentage
- Test with sample engineering values

**Formulas:**
- Stress = Force / Area
- Strain = ΔL / L₀
- Young's Modulus = Stress / Strain
- Heat Transfer = k × A × ΔT × t
- Efficiency = (Useful Output / Total Input) × 100

---

### **8. Data Processing Pipeline**

Create a complete data processing pipeline using multiple functions:

**Tasks:**
- Create a function `read_sensor_data()` that returns a list of sensor readings
- Create a function `filter_valid_readings(readings, min_val, max_val)` that filters readings within a range
- Create a function `calculate_statistics(readings)` that returns mean, max, min, and range
- Create a function `detect_anomalies(readings, threshold)` that finds readings more than threshold from mean
- Create a function `generate_report(statistics, anomalies)` that prints a formatted report
- Create a main function `process_sensor_data()` that uses all functions together

---

## **Example Solutions**

Here's how you might approach the first task:

```python
# Temperature Conversion Functions
print("=" * 50)
print("Task 1: Temperature Conversion Functions")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

# Test the functions
test_temps = [0, 25, 100]
print("Temperature conversions:")
for temp in test_temps:
    f = celsius_to_fahrenheit(temp)
    k = celsius_to_kelvin(temp)
    print(f"{temp}°C = {f}°F = {k}K")

def convert_temperature(temp, from_scale, to_scale):
    """Convert between any two temperature scales"""
    # First convert to Celsius
    if from_scale.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temp)
    elif from_scale.lower() == 'kelvin':
        celsius = temp - 273.15
    else:  # already celsius
        celsius = temp
    
    # Then convert to target scale
    if to_scale.lower() == 'fahrenheit':
        return celsius_to_fahrenheit(celsius)
    elif to_scale.lower() == 'kelvin':
        return celsius_to_kelvin(celsius)
    else:  # celsius
        return celsius

# Test the general conversion function
print(f"\n25°C to Fahrenheit: {convert_temperature(25, 'celsius', 'fahrenheit')}")
print(f"77°F to Kelvin: {convert_temperature(77, 'fahrenheit', 'kelvin')}")
```

---

## **Tips for Success**

- **Use descriptive function names** that clearly indicate what the function does
- **Add docstrings** to explain what each function does
- **Test your functions** with different input values
- **Use meaningful variable names** inside your functions
- **Keep functions focused** on doing one thing well
- **Use parameters** to make functions flexible and reusable
- **Return values** that can be used by other functions

---

## **What to Submit**

Create a Python file called `lab06_extra.py` with your solutions. For each task, write the functions and include test cases demonstrating they work correctly.

**Example structure:**
```python
# Lab 06 Extra: Practice with Functions for Engineers and Scientists

# Task 1: Temperature Conversion Functions
print("=" * 50)
print("Task 1: Temperature Conversion Functions")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # Your code here
    pass

# Test cases
print("Testing temperature conversions...")
# Your test code here...

# Task 2: Scientific Calculator Functions
print("\n" + "=" * 50)
print("Task 2: Scientific Calculator Functions")
print("=" * 50)

def calculate_area_circle(radius):
    """Calculate area of a circle"""
    # Your code here
    pass

# Continue for all tasks...
```

**Good luck and have fun practicing with functions in scientific contexts!**
