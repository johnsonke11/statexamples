import matplotlib.pyplot as plt
import math
def mean(sampleset):
    total = 0
    for element in sampleset:
        total = total + element
    return total/len(sampleset)
def variance(sampleset):
    total = 0
    setmean = mean(sampleset)
    for element in sampleset:
        total =total + (math.pow(element-setmean,2))
    return total/len(sampleset)
myset1=[2.,10.,3.,6.,4.,6.,10.]
myset2=[1.,-100.,15.,-100.,21.]
print("Variance of first set:" + str(variance(myset1)))
print("Variance of second set:" + str(variance(myset2)))
mymean=mean(myset1)
plt.plot(myset1)
plt.plot([mymean] * 7)
plt.show()