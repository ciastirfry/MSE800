import numpy as np

def main():
    # Temperature data in Celsius
    celsius_temps = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

    # 1. Calculate the average temperature
    avg_temp = np.mean(celsius_temps)
    print(f"Average temperature for the week: {avg_temp:.2f}°C")

    # 2. Find the highest and lowest temperatures
    max_temp = np.max(celsius_temps)
    min_temp = np.min(celsius_temps)
    print(f"Highest temperature: {max_temp}°C")
    print(f"Lowest temperature: {min_temp}°C")

    # 3. Convert temperatures to Fahrenheit
    fahrenheit_temps = celsius_temps * 9/5 + 32
    print("Temperatures in Fahrenheit:")
    print(np.round(fahrenheit_temps, 2))

    # 4. Find indices where temperature > 20°C
    hot_day_indices = np.where(celsius_temps > 20)[0]
    print("Indices of days with temperature > 20°C:")
    print(hot_day_indices)

if __name__ == "__main__":
    main()
