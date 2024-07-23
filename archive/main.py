import numpy as np
import matplotlib.pyplot as plt

from debug import debug
'''
1. Define the Complex Vector w: 
  - Create a complex vector with dimensions 256×1.
2. Define the Complex Array α(θ,ϕ): 
  - Create a complex 3D array with dimensions 256×361×91.
3. Compute the Conjugate Transpose of w
  - This is w^H , the Hermitian (complex conjugate transpose) of w
4. Perform the Matrix Multiplication: 
  - Multiply w^H with α(θ,ϕ)
'''
# ====================================================
# alpha dimensions
alpha_dim1 = 256
alpha_dim2 = 361
alpha_dim3 = 91
# ====================================================
w       = np.random.random((256, 1)) + 1j * np.random.random((256, 1))          # Define the Complex Vector w
alpha   = np.zeros((alpha_dim1, alpha_dim2, alpha_dim3), dtype=np.complex128)   # Define the Complex Array α(θ,ϕ)
F0      = np.empty((361, 91), dtype=np.complex128)                              # Define the target binary matrix
# ====================================================
# 3 Compute the Hermitian transpose (conjugate transpose) of w
w_H = np.conjugate(w.T)
# ====================================================
# 4 Perform the Matrix Multiplication:
# For each θ and ϕ pair, you will multiply w_H with the corresponding slice of αlpha:
for theta in range(alpha_dim2):
    for phi in range(alpha_dim3):
        # Extract the 256x1 slice for given theta, phi
        alpha_slice = alpha[:, theta, phi].reshape(-1, 1)
        # Compute the matrix product
        F0[theta, phi] = np.dot(w_H, alpha_slice)
        debug()
 

np.savetxt()


