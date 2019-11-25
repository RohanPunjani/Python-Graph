
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 20*(np.pi), .5)
y = np.sin(x)
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Sine Function')
plt.plot(x, y)
plt.show()
