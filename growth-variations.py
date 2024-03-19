import numpy as np
import matplotlib.pyplot as plt

def euler_maruyama(r, alpha, K, y0, dt, num_points):
    dW = np.sqrt(dt) * np.random.randn(num_points)
    y = np.zeros(num_points)
    y[0] = y0

    for i in range(1, num_points):
        drift = r * y[i-1] * (1 - y[i-1] / (alpha * K)) * dt
        diffusion = alpha * y[i-1] * dW[i-1]
        y[i] = y[i-1] + drift + diffusion

    return y

# Parameters
alpha_mean = 1.0
alpha_std = 0.1
K = 1000
y0 = 100
dt = 0.01
num_points = 5000

# Intrinsic growth rates (r values)
r_values = np.random.uniform(0, 2, 10)

# Plot for each r value
plt.figure(figsize=(10, 6))
for r in r_values:
    y = euler_maruyama(r, np.random.normal(alpha_mean, alpha_std), K, y0, dt, num_points)
    plt.plot(np.linspace(0, 3650, num_points), y, label=f'r = {r:.2f}')

plt.axhline(K, label='K', linestyle='--', color='red')
plt.xlabel('Time(day)', fontsize=15)
plt.ylabel('Population (y)', fontsize=15)
plt.xlim(0, 3650)
# plt.title('Stochastic Logistic Growth for Different Intrinsic Growth Rates (r)')
plt.legend(bbox_to_anchor=(1, 1), fontsize=10)
plt.show()
