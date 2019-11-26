
import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(0, 2*(np.pi), .5)
y1 = np.sin(x1)
x2 = np.arange(0, 2*(np.pi), .5)
y2 = np.cos(x2)
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Sine and Cosine Function')
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()
