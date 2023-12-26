import csv
import matplotlib.pyplot as plt

# Define file path
file_path = "weatherHistory.csv"

# Initialize empty list to store results
results = []

# Read data from file using DictReader
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Extract variables
        temperature = float(row["temperature"])
        humidity = float(row["humidity"])
        pressure = float(row["pressure"])

        # Define quadratic equation coefficients
        a = 0.01
        b = -0.5
        c = 25

        # Calculate weather parameter
        precipitation = a * temperature**2 + b * humidity + c

        # Store result
        results.append({
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "precipitation": precipitation
        })

# Plotting
temperature_values = [result["temperature"] for result in results]
precipitation_values = [result["precipitation"] for result in results]

plt.plot(temperature_values, precipitation_values, 'o', label='Weather Data')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation')
plt.title('Weather Data Analysis')
plt.legend()

# Save the plot to a file (e.g., PNG)
plt.savefig('weather_plot.png')

# Print results
for result in results:
    print(f"Temperature: {result['temperature']}°C, Humidity: {result['humidity']}%, "
          f"Pressure: {result['pressure']}hPa, Precipitation: {result['precipitation']}")

# Show the plot
plt.show() 
 
