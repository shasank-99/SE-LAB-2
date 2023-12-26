 import matplotlib.pyplot as plt
# Quadratic equation
temperature = 20.0
pressure = 800.0
humidity = 79.0
# Quadratic equation coefficients
a = 0.01
b = -0.5
c = 25
# Calculate weather parameter (e.g., precipitation)
precipitation = a * temperature**2 + b * humidity + c
# Generate x-axis values (temperature range)
temperature_range = range(0, 31)
# Calculate precipitation for each temperature value
precipitation_values = [
    a * temp**2 + b * humidity + c for temp in temperature_range
]
print(f"Precipitation: {precipitation}")
# Create plot
plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='o', linestyle='-')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.grid(True)
# Show plot
plt.show() 
