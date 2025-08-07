# polya urn

import random
import matplotlib.pyplot as plt

steps_input = input('total steps (default = 1000): ')
steps = int(steps_input) if steps_input.strip() else 1000

components_input = input('marbels number initial (default = 2): ')
components = int(components_input) if components_input.strip() else 2

initial_value_input = input('initial value: (default = 1) ')
initial_value = int(initial_value_input) if initial_value_input.strip() else 1


dick = {}
bag = []
bag_compo_num = components*initial_value
data = {}

for c in range(components):
    n = 'group' + str(c)
    for i in range(initial_value):
        bag.append(n)
    dick[n] = [initial_value]
    data[n] = [(initial_value/bag_compo_num)]

for s in range(steps):
    bag_compo_num += 1
    a = random.choice(bag)
    bag.append(a)

    for c in range(components):
        n = 'group' + str(c)
        count = bag.count(n)
        dick[n].append(count)
        data[n].append((count/bag_compo_num))

data = data #just in case you didn't know!

x = list(range(1, len(next(iter(data.values()))) + 1)) 
for key, values in data.items():
    plt.plot(x, values, marker='o', label=key)

plt.title("Comparison of Items Over Time")
plt.xlabel("Index")
plt.ylabel("Value")
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()
