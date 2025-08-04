# Week 1 - Activity 3: Rainfall Analysis with NumPy
# Student: Fredierick Saladas

## Tasks: 
    # Convert the list to a NumPy array and print it.
    # Print the total rainfall for the week.
    # Print the average rainfall for the week.
    # Count how many days had no rain (0 mm).
    # Print the days (by index) where the rainfall was more than 5 mm.
    # Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())


import numpy as np
def main():
    # 1. Sample rainfall data for 7 days (in millimeters)
    rainfall_list = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

    # 2. Convert the list to a NumPy array
    rainfall_array = np.array(rainfall_list)
    print("Rainfall array:", rainfall_array)

    # 3. Total rainfall for the week
    total_rainfall = np.sum(rainfall_array)
    print("Total rainfall for the week:", total_rainfall, "mm")

    # 4. Average rainfall for the week
    average_rainfall = np.mean(rainfall_array)
    print("Average rainfall for the week:", average_rainfall, "mm")

    # 5. Count how many days had no rain (0 mm)
    no_rain_days = np.sum(rainfall_array == 0.0)
    print("Number of days with no rain:", no_rain_days)

    # 6. Days with rainfall > 5 mm (show indices)
    heavy_rain_days = np.where(rainfall_array > 5.0)[0]
    print("Days with rainfall > 5 mm (by index):", heavy_rain_days)

    # 7. 75th percentile of rainfall and values above it
    percentile_75 = np.percentile(rainfall_array, 75)
    above_75 = rainfall_array[rainfall_array > percentile_75]
    print("75th percentile of rainfall:", percentile_75, "mm")
    print("Rainfall values above 75th percentile:", above_75)

if __name__ == "__main__":
    main()