# Task name: Daily Temperature Recording and Weekly Averages using 3D Matrices

# Define cities, days, and weeks
cities = ["Quito", "Guayaquil", "Cuenca"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num_weeks = 2

# 3D Matrix: [city][day][week]
temperatures = [
    [ [18, 19], [17, 18], [18, 20], [17, 19], [19, 20], [20, 21], [18, 19] ],  # Quito
    [ [28, 29], [29, 30], [30, 31], [28, 29], [30, 31], [31, 32], [29, 30] ],  # Guayaquil
    [ [15, 16], [14, 15], [16, 17], [15, 16], [17, 18], [18, 19], [16, 17] ]   # Cuenca
]

# Calculate and display averages
print("--- Weekly Temperature Averages by City ---")
for c in range(len(cities)):
    for w in range(num_weeks):
        total = 0
        for d in range(len(days)):
            total += temperatures[c][d][w]
        average = total / len(days)
        print(f"{cities[c]}, Week {w+1}: Average = {average:.2f}°C")

