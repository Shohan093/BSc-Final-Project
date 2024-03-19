import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.1
K = 1000
y0 = 100
alpha_mean = np.linspace(0.1, 1, 10)
alpha_std = np.linspace(0.01, 0.2, 10)
sigma = 0.1

# Time parameters
t_start = 0
t_end = 3650
num_points = 5000
dt = (t_end - t_start) / num_points

# Generate Wiener increments
dW = np.sqrt(dt) * np.random.randn(num_points)

# Initialize arrays
t = np.linspace(t_start, t_end, num_points)
y = np.zeros_like(t)
y[0] = y0

sim_num = 10

for x in range(sim_num):
    alpha_values = alpha_mean[x] + alpha_std[x] * np.random.randn(num_points)
    for i in range(1, num_points):
        drift = r * y[i - 1] * (1 - y[i - 1] / (alpha_values[i] * K)) * dt
        diffusion = sigma * y[i - 1] * dW[i - 1]
        y[i] = y[i - 1] + drift + diffusion
    
    plt.plot(t, y, label=f'Simulation {x + 1}')
    y[0] = y0

# Plot the solution
# plt.plot(t, y, label='Population density')
plt.axhline(K, label='K', linestyle='--', color='red')
plt.xlabel('Time(day)', fontsize=15)
plt.ylabel('Population', fontsize=15)
plt.xlim(0, t_end)
# plt.title('Stochastic Logistic Growth with Euler-Maruyama Method')
plt.legend(bbox_to_anchor=(1, 1), fontsize=10)
plt.show()
