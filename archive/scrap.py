

'''
1. Loading Configuration:           Reads dimensions and other parameters from a YAML file.
2. Initializing Variables:          Initializes complex arrays for w, alpha, and F0.
3. Defining Constants and           Functions: Sets up necessary constants like k0 and defines the function f(theta, phi).
4. Computing Alpha:                 Calculates alpha based on the given formula.
5. Gradient Descent Optimization:   Performs gradient descent to update the vector w and minimize
'''

import numpy as np
import yaml

# Load the configuration from the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract dimensions from the configuration
alpha_dim1 = config['dimensions']['alpha']['dim1']
alpha_dim2 = config['dimensions']['alpha']['dim2']
alpha_dim3 = config['dimensions']['alpha']['dim3']
w_rows = config['dimensions']['w']['rows']
w_cols = config['dimensions']['w']['cols']
F0_dim1 = config['dimensions']['F0']['dim1']
F0_dim2 = config['dimensions']['F0']['dim2']

# Define the size of the arrays
alpha_shape = (alpha_dim1, alpha_dim2, alpha_dim3)
w_shape = (w_rows, w_cols)
F0_shape = (F0_dim1, F0_dim2)

# Initialize w, alpha, and F0 pseudo numbers
w = np.random.rand(w_shape[0], w_shape[1]) + 1j * np.random.rand(w_shape[0], w_shape[1])
F0 = np.random.rand(F0_shape[0], F0_shape[1]) + 1j * np.random.rand(F0_shape[0], F0_shape[1])
alpha = np.empty(alpha_shape, dtype=np.complex128)

# Define constants and functions
k0 = 1  # Example value, should be defined as per your problem
x_i = np.linspace(0, 1, alpha_dim1)  # Example values, should be defined as per your problem
y_i = np.linspace(0, 1, alpha_dim1)  # Example values, should be defined as per your problem

def f(theta, phi):
    # Example function, should be defined as per your problem
    return np.ones(alpha_dim1)

# Compute alpha(theta, phi)
theta_range = np.deg2rad(np.arange(0, 361, 1))  # Convert degrees to radians
phi_range = np.deg2rad(np.arange(0, 91, 1))  # Convert degrees to radians

for i, theta in enumerate(theta_range):
    for j, phi in enumerate(phi_range):
        alpha[:, i, j] = f(theta, phi) * np.exp(-1j * k0 * (x_i * np.sin(theta) * np.cos(phi) + y_i * np.sin(theta) * np.sin(phi)))

# Compute the Hermitian transpose (conjugate transpose) of w
w_H = np.conjugate(w.T)

# Define the learning rate
eta = 0.01

# Define the maximum number of iterations for the gradient descent
max_iterations = 1

# Define the target normalized amplitude pattern, Q_s
Q_s = np.ones(F0_shape)  # Example values, should be defined as per your problem

# Optimization loop
for iteration in range(max_iterations):
    J_MV = 0
    gradient = np.zeros(w.shape, dtype=np.complex128)
    
    # Compute the cost function J_MV and its gradient
    for theta in range(alpha_dim2):
        for phi in range(alpha_dim3):
            # Extract the 256x1 slice for given theta, phi
            alpha_slice = alpha[:, theta, phi].reshape(-1, 1)
            F_theta_phi = np.dot(w_H, alpha_slice)
            F_max = np.max(np.abs(F_theta_phi))
            error = np.abs(F_theta_phi - F0[theta, phi] * np.exp(1j * np.angle(F_theta_phi) / F_max)) ** 2
            J_MV += error
            
            # Compute the gradient
            gradient += 2 * (F_theta_phi - F0[theta, phi] * np.exp(1j * np.angle(F_theta_phi) / F_max)) * np.conjugate(alpha_slice)
    
    # Update the weights w
    w = w - eta * gradient
    
    # Print the cost function value every 100 iterations
    if iteration % 100 == 0:
        print(f"Iteration {iteration}, J_MV = {J_MV}")

# Print the optimized weights
print("Optimized weights w:")
print(w)
