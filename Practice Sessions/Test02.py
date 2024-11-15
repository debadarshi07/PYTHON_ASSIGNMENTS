from random import randrange as rr
from matplotlib import pyplot as plt
from random import random as r

# simulation of data
rolls = [rr(1, 7) for _ in range(60000)]

# getting all the possible unique values
unique_values = []
for value in rolls:
    if value not in unique_values:
        unique_values.append(value)
        
# sort the list of unique values -- x axis entries
unique_values = sorted(unique_values)

# find the frequency of each unique values in rolls -- y axis entries
frequencies = [rolls.count(value) for value in unique_values]
print(frequencies)

# Create bargraph
title = f"Rolling a fair six-sided die {len(rolls)} times"
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'violet']
random_colors = [tuple(r() for _ in range(3)) for _ in range(6)]
plt.bar(unique_values, frequencies, color = random_colors)
plt.title(title)
plt.xlabel('Possible outcomes')
plt.ylim(top = max(frequencies) * 1.15)
# plt.xlim(right = max(unique_values) * 1.2)
plt.ylabel('Frequencies')
for i in range(len(unique_values)):
    plt.text(unique_values[i], frequencies[i], f"{frequencies[i]}\n{frequencies[i]/len(rolls):.2%}", ha = 'center', va = 'bottom')
plt.show()