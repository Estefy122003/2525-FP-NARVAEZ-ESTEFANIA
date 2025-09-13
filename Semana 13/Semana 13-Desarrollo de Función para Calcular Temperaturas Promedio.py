# ============================
# Function to calculate the average temperature for each city
# ============================

def average_temperature(cities_temperatures):
    """
    Calculates the average temperature of each city over multiple weeks.

    Args:
        cities_temperatures (dict): Dictionary with city names as keys and a list of weeks as values.
                                     Each week is a list of daily temperatures.
    Returns:
        dict: Dictionary with city names as keys and their overall average temperature as values.
    """
    average_temps = {}

    for city, weeks in cities_temperatures.items():
        # Flatten all weeks into a single list of temperatures
        all_temps = [temp for week in weeks for temp in week]
        avg = sum(all_temps) / len(all_temps)
        average_temps[city] = avg

    return average_temps


# ============================
# Example data: 3 cities, 4 weeks, 7 days each week
# ============================

cities_temperatures = {
    "Quito": [
        [18, 19, 20, 21, 20, 19, 18],  # Week 1
        [19, 20, 21, 22, 20, 19, 18],  # Week 2
        [18, 19, 19, 20, 21, 20, 19],  # Week 3
        [20, 21, 22, 22, 21, 20, 19]   # Week 4
    ],
    "Guayaquil": [
        [28, 29, 30, 31, 29, 28, 27],
        [29, 30, 31, 32, 30, 29, 28],
        [30, 31, 32, 33, 31, 30, 29],
        [31, 32, 33, 34, 32, 31, 30]
    ],
    "Cuenca": [
        [15, 16, 17, 16, 15, 14, 15],
        [16, 17, 18, 17, 16, 15, 16],
        [15, 16, 16, 17, 16, 15, 14],
        [16, 17, 17, 18, 17, 16, 15]
    ]
}

# ============================
# Calculate averages
# ============================

averages = average_temperature(cities_temperatures)

# ============================
# Display results
# ============================

print("=== Average Temperatures by City ===")
for city, avg in averages.items():
    print(f"{city}: {avg:.2f}°C")



