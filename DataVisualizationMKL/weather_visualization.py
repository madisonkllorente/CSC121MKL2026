# Weather Visualization MKL

import matplotlib.pyplot as plt

# Months
months = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

# Average Asheville high temperatures in Fahrenheit
highs = [47, 51, 60, 69, 76, 83, 86, 85, 79, 69, 59, 49]

# Create graph
plt.figure(figsize=(10, 6))

plt.plot(months, highs, marker='o', c='red')

# Add labels and title
plt.title("Asheville Monthly High Temperatures", fontsize=20)

plt.xlabel("Month", fontsize=16)
plt.ylabel("Temperature (°F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=12)

# Display graph
plt.show()