# bifurcation for alpha vs x
from click import style
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the logistic growth model
def logistic_growth(y, t, r, K, alpha):
    dydt = r * y * (1 - y / (K * alpha))
    return dydt

# Bifurcation analysis function
def bifurcation_analysis(r_values, y0, K, t_max, t_points, alpha):
    bifurcation_data = {"alpha": [], "y": []}

    for al in alpha:
        if al == 0:
            pass
        else:
            # Solve the ODE for each value of r
            sol = odeint(logistic_growth, y0, np.linspace(0, t_max, t_points), args=(r_values, K, al))

            # Extract the last few points to observe the long-term behavior
            y_steady_state = sol[-int(t_points / 10):, 0]

            # Store data for bifurcation plot
            bifurcation_data["alpha"].extend([al] * len(y_steady_state))
            bifurcation_data["y"].extend(y_steady_state)

    return bifurcation_data

# Set parameters
r_values = 0.1
y0 = 10  # Initial condition
K = 100000    # Carrying capacity
t_max = 100  # Maximum time
t_points = 1000  # Number of time points
alpha = np.linspace(0, 10, 500) # stochastic parameter

# Perform bifurcation analysis
bifurcation_data = bifurcation_analysis(r_values, y0, K, t_max, t_points, alpha)

# print(bifurcation_data)

# Plot the bifurcation diagram
plt.figure(figsize=(8, 6))
plt.scatter(bifurcation_data["alpha"], bifurcation_data["y"], s=0.1, color='black')
plt.xlabel('stochastic parameter(alpha)', fontsize=15)
plt.ylabel('Population (N)', fontsize=15)
# plt.title('Bifurcation Diagram - Logistic Growth Stochastic Model')
plt.show()
