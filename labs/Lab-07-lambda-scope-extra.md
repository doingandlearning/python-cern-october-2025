# **Lab 07 Extra: Lambda Functions, Scope, and Practical Applications for Engineers and Scientists**

## **Objective**
This extra lab focuses on practical applications of lambda functions, understanding variable scope (local vs global), and solving real-world problems that engineers and scientists encounter. You will learn when and why to use lambda functions effectively.

You will:
1. **Use lambda functions** for sorting and data processing
2. **Understand scope** - local vs global variables
3. **Apply lambdas** to scientific data analysis
4. **Solve practical problems** with lambda functions
5. **Learn best practices** for when to use lambdas vs regular functions

---

## **Tasks**

### **1. Sorting Scientific Data with Lambdas**

Work with experimental data and use lambdas for sorting:

```python
# Sample experimental data: (experiment_id, temperature, pressure, result)
experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    ("EXP_003", 22.8, 103.1, 0.78),
    ("EXP_004", 28.5, 99.8, 0.88),
    ("EXP_005", 26.7, 102.3, 0.91)
]
```

**Tasks:**
- Sort experiments by temperature (ascending)
- Sort experiments by pressure (descending)
- Sort experiments by result (descending)
- Sort experiments by experiment ID alphabetically
- Create a custom sort that prioritizes high results AND low temperatures

---

### **2. Scope Practice with Scientific Calculations**

Create functions that demonstrate local vs global scope:

```python
# Global variables
PI = 3.14159
GRAVITY = 9.81  # m/s²
```

**Tasks:**
- Create a function `calculate_circle_area(radius)` that uses the global PI
- Create a function `calculate_pendulum_period(length)` that uses global GRAVITY
- Inside the pendulum function, create a local variable `frequency` and calculate it
- Create a function that modifies a global counter for experiment tracking
- Demonstrate what happens when you try to modify global variables vs local variables

---

### **3. Lambda Functions for Data Processing**

Process sensor readings using lambda functions:

```python
# Sample sensor data: (sensor_id, reading, timestamp, status)
sensor_data = [
    ("SENSOR_A", 23.5, "10:30", "OK"),
    ("SENSOR_B", 25.1, "10:31", "WARNING"),
    ("SENSOR_C", 22.8, "10:32", "OK"),
    ("SENSOR_D", 26.3, "10:33", "ERROR"),
    ("SENSOR_E", 24.7, "10:34", "OK")
]
```

**Tasks:**
- Use lambda to extract just the readings from sensor data
- Use lambda to find sensors with "OK" status
- Use lambda to calculate readings above 24°C
- Use lambda to create a list of (sensor_id, reading) tuples for error sensors
- Use lambda to sort sensors by reading value

---

### **4. Practical Engineering Applications**

Solve real engineering problems with lambdas:

```python
# Sample material data: (material, density, strength, cost_per_kg)
materials = [
    ("Steel", 7850, 400, 2.50),
    ("Aluminum", 2700, 200, 3.20),
    ("Titanium", 4500, 900, 25.00),
    ("Carbon_Fiber", 1600, 600, 45.00),
    ("Wood", 600, 50, 0.80)
]
```

**Tasks:**
- Sort materials by strength-to-weight ratio (strength/density)
- Find materials cheaper than $5 per kg
- Sort materials by cost efficiency (strength/cost)
- Create a lambda to calculate strength per dollar
- Sort materials by density (lightest first)

---

### **5. Scope and Function Composition**

Create functions that demonstrate scope and use lambdas:

```python
# Global experiment counter
experiment_count = 0
```

**Tasks:**
- Create a function `run_experiment()` that increments the global counter
- Inside `run_experiment()`, create local variables for temperature and pressure
- Create a nested function `calculate_efficiency()` that uses the local variables
- Use lambda inside the nested function to calculate a derived value
- Demonstrate how local variables are not accessible outside their scope

---

### **6. Lambda Functions for Statistical Analysis**

Use lambdas for quick statistical calculations:

```python
# Sample measurement data
measurements = [12.3, 15.7, 18.2, 14.1, 16.8, 13.9, 17.4, 15.2, 19.1, 14.6]
```

**Tasks:**
- Use lambda with `max()` and `min()` to find extreme values
- Use lambda with `sorted()` to sort measurements
- Use lambda with `filter()` to find measurements above 15
- Use lambda with `map()` to convert measurements to a different scale
- Create a lambda to calculate deviations from the mean

---

### **7. Complex Sorting with Multiple Criteria**

Sort complex data using lambdas with multiple sorting criteria:

```python
# Sample equipment data: (name, age_years, efficiency, maintenance_cost)
equipment = [
    ("Pump_A", 5, 0.85, 1200),
    ("Pump_B", 3, 0.92, 800),
    ("Pump_C", 8, 0.78, 1500),
    ("Pump_D", 2, 0.95, 600),
    ("Pump_E", 6, 0.88, 1100)
]
```

**Tasks:**
- Sort by efficiency (highest first), then by age (lowest first)
- Sort by maintenance cost per year of age
- Sort by overall score: efficiency - (age/10) - (maintenance_cost/10000)
- Create a lambda to calculate "value score" (efficiency/cost)
- Sort by value score (highest first)

---

### **8. Scope Demonstration with Nested Functions**

Create a comprehensive example showing scope in action:

**Tasks:**
- Create a global variable `lab_temperature = 22.0`
- Create a function `analyze_sample()` that takes a sample temperature
- Inside `analyze_sample()`, create local variables for analysis
- Create a nested function `calculate_deviation()` that uses both global and local variables
- Use lambda inside the nested function for calculations
- Demonstrate variable shadowing by creating local variables with same names as globals

---

## **Key Concepts to Focus On**

### **Lambda Functions**
- **Use for simple, one-time operations**
- **Great for sorting with custom keys**
- **Useful with built-in functions like `sorted()`, `max()`, `min()`**
- **Don't overuse - regular functions are often clearer**

### **Scope (Local vs Global)**
- **Global variables** are accessible everywhere
- **Local variables** are only accessible within their function
- **You can read globals** from inside functions
- **You need `global` keyword** to modify globals from inside functions
- **Local variables shadow** global variables with the same name

### **When to Use Lambdas**
- **Sorting with custom criteria**
- **Simple transformations** with `map()`
- **Simple filtering** with `filter()`
- **One-time calculations** that don't need a full function

---

## **Tips for Success**

- **Start with simple lambdas** and build complexity gradually
- **Use meaningful variable names** in lambda expressions
- **Test your scope understanding** by printing variables at different points
- **Remember that lambdas are just anonymous functions**
- **Don't make lambdas too complex** - use regular functions instead
- **Practice with real data** that engineers and scientists would use

---

## **What to Submit**

Create a Python file called `lab07_extra.py` with your solutions. For each task, write the code and include comments explaining what you're doing.

**Example structure:**
```python
# Lab 07 Extra: Lambda Functions, Scope, and Practical Applications

# Task 1: Sorting Scientific Data with Lambdas
print("=" * 50)
print("Task 1: Sorting Scientific Data with Lambdas")
print("=" * 50)

experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    # ... more data
]

# Your code here...

# Task 2: Scope Practice with Scientific Calculations
print("\n" + "=" * 50)
print("Task 2: Scope Practice")
print("=" * 50)

# Global variables
PI = 3.14159

# Your code here...

# Continue for all tasks...
```

**Good luck and have fun with lambdas and scope!**
