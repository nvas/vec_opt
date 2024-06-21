import numpy as np

# Input parameters
w = np.random.randn(256) + 1j * np.random.randn(256)  # Initial complex vector w
alpha = np.zeros((256, 361, 91), dtype=np.complex128)  # Initialize alpha
F0 = np.zeros((361, 91), dtype=np.complex128)  # Target binary coding matrix

# Constants
k0 = 1  # example value, replace with actual
x_i = np.linspace(-1, 1, 256)  # example values, replace with actual
y_i = np.linspace(-1, 1, 256)  # example values, replace with actual
U = 1  # example value, replace with actual
theta_range = np.deg2rad(np.arange(0, 361, 1))
phi_range = np.deg2rad(np.arange(0, 91, 1))

# Define alpha
def compute_alpha(theta, phi):
    return np.exp(-1j * k0 * (x_i * np.sin(theta) * np.cos(phi) + y_i * np.sin(theta) * np.sin(phi)))

# Compute F
def compute_F(w, alpha):
    return np.einsum('i,ijk->jk', np.conjugate(w), alpha)

# Target function
def J_MV(w, alpha, F0):
    F = compute_F(w, alpha)
    F_max = np.max(np.abs(F))
    zeta = np.angle(F)
    integrand = np.abs(F - F0 * np.exp(1j * zeta) * F_max) ** 2
    return np.trapz(np.trapz(integrand, phi_range), theta_range)

# Gradient descent optimization
def optimize_w(w, alpha, F0, eta, num_iterations):
    for _ in range(num_iterations):
        grad_w = compute_gradient(w, alpha, F0)
        w = w - eta * grad_w
    return w

# Gradient of the cost function
def compute_gradient(w, alpha, F0):
    F = compute_F(w, alpha)
    F_max = np.max(np.abs(F))
    zeta = np.angle(F)
    R_s = compute_R_s(alpha)
    R_k = compute_R_k(alpha, F0, F_max, zeta)
    R_0k = compute_R_0k(F0, F_max)
    grad = 2 * (R_s @ w - R_k)
    return grad

# Compute R_s
def compute_R_s(alpha):
    integral_target = np.trapz(np.trapz(np.einsum('ijk,ijl->ikl', alpha, alpha.conj()), phi_range), theta_range)
    integral_non_target = np.trapz(np.trapz(np.einsum('ijk,ijl->ikl', alpha, alpha.conj()), phi_range), theta_range)
    return integral_target + U * integral_non_target

# Compute R_k
def compute_R_k(alpha, F0, F_max, zeta):
    integrand = alpha * F0 * np.exp(-1j * zeta)
    return F_max * np.trapz(np.trapz(integrand, phi_range), theta_range)

# Compute R_0k
def compute_R_0k(F0, F_max):
    return F_max**2 * np.trapz(np.trapz(F0**2, phi_range), theta_range)

# Example usage
alpha = np.array([compute_alpha(theta, phi) for theta in theta_range for phi in phi_range]).reshape(256, 361, 91)
optimized_w = optimize_w(w, alpha, F0, eta=0.01, num_iterations=1000)

print("Optimized w:", optimized_w)
