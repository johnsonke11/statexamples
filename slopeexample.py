import matplotlib.pyplot as plt
import numpy as np
def quadratic(var):
    return 2* pow(var,2)
x=np.arange(0,.5,.1)
plt.plot(x,quadratic(x))
plt.plot([1,4], [quadratic(1), quadratic(4)], linewidth=2.0)
plt.plot([1,4], [quadratic(1), quadratic(1)], linewidth=3.0, label="Change in X")
plt.plot([4,4], [quadratic(1), quadratic(4)], linewidth=3.0, label="Change in y")

plt.legend()
plt.plot(x,10*x -8)
plt.show()