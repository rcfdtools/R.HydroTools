# Calculating a Continuous PDF (Normal Distribution)
# For a continuous distribution like the Normal (Gaussian) distribution, the Probability Density Function (PDF) is given by the formula:\(f(x)=\frac{1}{\sigma \sqrt{2\pi }}e^{-\frac{(x-\mu )^{2}}{2\sigma ^{2}}}\) where \(\mu \) is the mean and \(\sigma \) is the standard deviation.

import numpy as np
import math
import matplotlib.pyplot as plt

def normal_pdf(x, mean, std_dev):
    """
    Calculates the probability density function for a normal distribution manually.
    """
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    exponent = -((x - mean)**2) / (2 * std_dev**2)
    return coefficient * math.exp(exponent)

# Parameters for the distribution (e.g., standard normal distribution)
#mu = 0
#sigma = 1
mu = 105.801
sigma = 38.22773578 # STDEV.P from Excel

# Generate a range of x values
#x_values = np.linspace(-4, 4, 20)
x_values = [37.5273,40,46,62,65,71,73,80,80,81.1,82,85,85,89,90,90,90,91,95,96,100,108,109,110,110,120,120.1,122,134.5,135,136,148,150,150,150,150,155,160,230]
print(f'x values:\n{x_values}')

# Calculate the PDF for each x value
pdf_values = [normal_pdf(x, mu, sigma) for x in x_values]
print(f'pdf values:\n{pdf_values}')

# Plot the distribution
plt.figure(figsize=(8, 5))
plt.plot(x_values, pdf_values, color='red', label=f'PDF (mu={mu}, sigma={sigma})')
plt.title('Manually Calculated Normal PDF')
plt.xlabel('X value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
