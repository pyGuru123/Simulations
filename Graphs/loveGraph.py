import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 1000)
y = np.linspace(-3, 3, 1000)

l = 1 / x
o = np.sqrt(-y ** 2 + 9)
v = abs(-2 * y)
e = -3 * abs(np.sin(y))

plt.suptitle("python is ❤️")

plt.subplot(2,2,1)
plt.axis("off")
plt.plot(x, l, c='g')

plt.subplot(2,2,2)
plt.axis("off")
plt.plot(x, o, c='b')
plt.plot(x, -o, c='b')

plt.subplot(2,2,3)
plt.axis("off")
plt.plot(x, v, c='r')

plt.subplot(2,2,4)
plt.plot(e, y, c='m')
plt.axis("off")

plt.show()