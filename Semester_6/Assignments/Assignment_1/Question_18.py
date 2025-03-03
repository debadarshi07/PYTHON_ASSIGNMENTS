import pandas as pd
import matplotlib.pyplot as plt

celsius_temperatures = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
celsius_to_kelvin = lambda celsius: celsius + 273.15
kelvin_temperatures = list(map(celsius_to_kelvin, celsius_temperatures))

temperature_df = pd.DataFrame({
    'Celsius': celsius_temperatures,
    'Kelvin': kelvin_temperatures
})

print("Temperature Conversion Table:")
print(temperature_df)

plt.figure(figsize=(8, 6))
plt.plot(temperature_df['Celsius'], temperature_df['Kelvin'], marker='o', linestyle='-', color='b')
plt.title("Celsius to Kelvin Conversion")
plt.xlabel("Temperature (Celsius)")
plt.ylabel("Temperature (Kelvin)")
plt.grid(True)
plt.show()