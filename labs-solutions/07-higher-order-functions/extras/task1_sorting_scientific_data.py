# Lab 07 Extra - Task 1: Sorting Scientific Data with Lambdas
# Practice with lambda functions for sorting experimental data

print("=" * 50)
print("Task 1: Sorting Scientific Data with Lambdas")
print("=" * 50)

# Sample experimental data: (experiment_id, temperature, pressure, result)
experiments = [
    ("EXP_001", 25.3, 101.2, 0.85),
    ("EXP_002", 30.1, 98.7, 0.92),
    ("EXP_003", 22.8, 103.1, 0.78),
    ("EXP_004", 28.5, 99.8, 0.88),
    ("EXP_005", 26.7, 102.3, 0.91)
]

print("Original experimental data:")
for exp in experiments:
    print(f"  {exp[0]}: Temp={exp[1]}°C, Pressure={exp[2]}kPa, Result={exp[3]}")

# Sort by temperature (ascending)
sorted_by_temp = sorted(experiments, key=lambda x: x[1])
print(f"\nSorted by temperature (ascending):")
for exp in sorted_by_temp:
    print(f"  {exp[0]}: {exp[1]}°C")

# Sort by pressure (descending)
sorted_by_pressure = sorted(experiments, key=lambda x: x[2], reverse=True)
print(f"\nSorted by pressure (descending):")
for exp in sorted_by_pressure:
    print(f"  {exp[0]}: {exp[2]}kPa")

# Sort by result (descending)
sorted_by_result = sorted(experiments, key=lambda x: x[3], reverse=True)
print(f"\nSorted by result (descending):")
for exp in sorted_by_result:
    print(f"  {exp[0]}: {exp[3]}")

# Sort by experiment ID alphabetically
sorted_by_id = sorted(experiments, key=lambda x: x[0])
print(f"\nSorted by experiment ID (alphabetical):")
for exp in sorted_by_id:
    print(f"  {exp[0]}: {exp[1]}°C, {exp[2]}kPa, {exp[3]}")

# Custom sort: high results AND low temperatures
# Use negative result for descending, positive temperature for ascending
custom_sorted = sorted(experiments, key=lambda x: (-x[3], x[1]))
print(f"\nCustom sort (high result, low temperature):")
for exp in custom_sorted:
    print(f"  {exp[0]}: Result={exp[3]}, Temp={exp[1]}°C")

# Additional sorting examples
print(f"\nAdditional sorting examples:")

# Sort by pressure-to-temperature ratio
pressure_temp_ratio = sorted(experiments, key=lambda x: x[2]/x[1], reverse=True)
print("Sorted by pressure-to-temperature ratio (highest first):")
for exp in pressure_temp_ratio:
    ratio = exp[2]/exp[1]
    print(f"  {exp[0]}: Ratio={ratio:.3f}")

# Sort by result efficiency (result per degree temperature)
result_efficiency = sorted(experiments, key=lambda x: x[3]/x[1], reverse=True)
print("\nSorted by result efficiency (result per degree):")
for exp in result_efficiency:
    efficiency = exp[3]/exp[1]
    print(f"  {exp[0]}: Efficiency={efficiency:.4f}")

# Sort by multiple criteria: result (desc), then temperature (asc), then pressure (desc)
multi_criteria = sorted(experiments, key=lambda x: (-x[3], x[1], -x[2]))
print("\nMulti-criteria sort (result desc, temp asc, pressure desc):")
for exp in multi_criteria:
    print(f"  {exp[0]}: Result={exp[3]}, Temp={exp[1]}°C, Pressure={exp[2]}kPa")

print("\n" + "=" * 50)
print("Task 1 completed successfully!")
print("=" * 50)
