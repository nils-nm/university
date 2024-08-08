import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


matplotlib.use('Qt5Agg')


color = '#fc4f30'



#Max = 2.20
#Min = 1.39
n = 6
bins = [i/100 for i in range(135, 225, 2)]
print(bins, len(bins))

data = pd.read_csv('data.csv')
Max = max(data['Date'])
Min = min(data['Date'])

width = ((Max - Min)/10)
print(round(np.mean(data['Date']), 2))

#sigma = np.std(data['Date'])


def gauss(x, amp, mu, sigma):
    return amp*np.exp(-(x-mu)**2/(2*sigma**2))

x = np.linspace(Min, Max, n)



fig, ax = plt.subplots()



y, bins, patches = ax.hist(data['Date'], bins=n, histtype='barstacked')



popt, pcov = curve_fit(gauss, x, y, p0=(80, 25, 5))
#print(popt)

y = gauss(x, popt[0], popt[1], popt[2])


plt.plot(x, y,color='red')


# ------------------------------
fig.tight_layout()
plt.title('Test plot')
plt.xlabel('X')
plt.ylabel('Y')


plt.show(block=True)
