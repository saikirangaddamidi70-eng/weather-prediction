import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("weather.csv")

print("Weather data sample:")
print(data.head())

# Clean column names
print("\nColumns before strip:", data.columns)
data.columns = data.columns.str.strip()
print("Columns after strip:", data.columns)

# Drop missing values
data = data.dropna()

# Convert columns to float
data["Temperature"] = data["Temperature"].astype(float)
data["Humidity"] = data["Humidity"].astype(float)
data["Pressure"] = data["Pressure"].astype(float)

# Weather statistics
print("\nWeather Statistics:")
print("Average Temperature:", round(data["Temperature"].mean(), 2))
print("Average Humidity:", round(data["Humidity"].mean(), 2))
print("Average Pressure:", round(data["Pressure"].mean(), 2))

# Plot temperature trend
plt.figure(figsize=(8, 5))
plt.plot(data["Date"], data["Temperature"], marker="o", color="orange")
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Rule-based weather intelligence
def weather_rule(temperature, humidity, pressure):
    if humidity > 80 and pressure < 1010:
        return "High chance of Rain"
    elif temperature > 33:
        return "Hot weather"
    elif temperature < 25:
        return "Cold weather"
    else:
        return "Moderate weather"

data["Weather_Status"] = data.apply(
    lambda row: weather_rule(
        row["Temperature"], row["Humidity"], row["Pressure"]
    ),
    axis=1
)

print("\nWeather Insights:")
print(data[["Date", "Weather_Status"]])

# Weather explanation system
def explain_weather(humidity, pressure):
    if humidity > 80 and pressure < 1010:
        return "High humidity and low pressure indicate possible rainfall."
    elif humidity < 60:
        return "Low humidity suggests dry weather."
    else:
        return "Weather conditions are normal."

data["Explanation"] = data.apply(
    lambda row: explain_weather(row["Humidity"], row["Pressure"]),
    axis=1
)

print("\nWeather Explanation:")
print(data[["Date", "Explanation"]])

print("\n✅ Smart Weather Intelligence System Completed Successfully!")
