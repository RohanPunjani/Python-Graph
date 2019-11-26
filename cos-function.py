
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 2*(np.pi), .5)
y = np.cos(x)
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Cosine Function')
plt.plot(x, y)
plt.show()
