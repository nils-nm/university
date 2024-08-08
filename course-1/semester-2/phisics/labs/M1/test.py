import matplotlib.pyplot as plt
import numpy as np
import csv


#with open("data.csv", 'r') as x:
#    sample_data = list(csv.reader(x))

#rng = np.array(sample_data)
rng = np.random.default_rng(19680801)
#rng = np.loadtxt('data.csv', dtype=int)


# example data
mu = 25  # mean of distribution
sigma = 10  # standard deviation of distribution
x = rng.normal(loc=mu, scale=sigma, size=820)

num_bins = 42

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Value')
ax.set_ylabel('Probability density')
ax.set_title('Histogram of normal distribution sample: '
             fr'$\mu={mu:.0f}$, $\sigma={sigma:.0f}$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
