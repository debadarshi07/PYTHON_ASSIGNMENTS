from matplotlib import pyplot as plt
from random import random as r

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

response_labels = sorted({x for x in responses})

frequencies = [responses.count(label) for label in response_labels]

title = f"Response Frequencies"
plt.title(title)
plt.xlabel('Responses')
plt.ylabel('Frequencies')
for i in range(len(response_labels)):
    plt.text(response_labels[i], frequencies[i], f"{100 * frequencies[i] / len(responses)}", ha = 'center', va = 'bottom')

random_colors = [tuple(r() for _ in range(3)) for _ in range(6)]
plt.bar(response_labels, frequencies, color = random_colors)
plt.show()