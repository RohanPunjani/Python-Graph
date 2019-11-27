import matplotlib.pyplot as plt
slices = [7, 2, 2, 13]
# slices? -> They are just PIZZA slices of different sizes :p
activities = ['sleeping', 'eating', 'working', 'playing']
# name of the specific slice -> toppings on PIZZA
cols = ['c', 'm', 'r', 'b']
# color of Toppings
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.title('Making Pie Chart')
plt.show()
