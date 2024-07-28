import numpy as np
import matplotlib.pyplot as plt

def plot_complex_vector(w, title):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(np.real(w), 'b-o')
    plt.title(f'Real Part of {title}')
    plt.xlabel('Index')
    plt.ylabel('Real Value')

    plt.subplot(1, 2, 2)
    plt.plot(np.imag(w), 'r-o')
    plt.title(f'Imaginary Part of {title}')
    plt.xlabel('Index')
    plt.ylabel('Imaginary Value')
    
    plt.tight_layout()
    plt.show()

def plot_F(F, title):
    plt.figure(figsize=(10, 8))
    plt.imshow(np.abs(F), extent=[0, 360, 0, 90], aspect='auto', cmap='viridis')
    plt.colorbar(label='Magnitude')
    plt.title(f'{title} Magnitude')
    plt.xlabel('Theta (degrees)')
    plt.ylabel('Phi (degrees)')
    plt.show()
