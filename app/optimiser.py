#!/usr/bin/env python3
"""
Author: Sajid Fadlelseed
Date: 2024-07-23
Description: This script performs gradient descent optimisation based on a specified configuration file.
It initializes variables, defines constants, and carries out the optimization process with parameters
specified in the configuration file.

Usage:
    python optimiser.py
"""

import numpy as np
import yaml


class OptimizationConfig:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.alpha_shape = (
            self.config['dimensions']['alpha']['dim1'],
            self.config['dimensions']['alpha']['dim2'],
            self.config['dimensions']['alpha']['dim3']
        )
        self.w_shape = (
            self.config['dimensions']['w']['dim1'],
            self.config['dimensions']['w']['dim2']
        )
        self.F0_shape = (
            self.config['dimensions']['F0']['dim1'],
            self.config['dimensions']['F0']['dim2']
        )

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

class GradientDescentoptimiser:
    def __init__(self, config_path):
        self.config = OptimizationConfig(config_path)
        self.k0 = 1  # Peseudo-data
        self.eta = 0.01
        self.max_iterations = 1
        self.Q_s = np.ones(self.config.F0_shape)  # Peseudo-data

        self.initialize_variables()
        self.define_constants()

    def initialize_variables(self):
        self.w = np.random.rand(*self.config.w_shape) + 1j * np.random.rand(*self.config.w_shape)
        self.F0 = np.random.rand(*self.config.F0_shape) + 1j * np.random.rand(*self.config.F0_shape)
        self.alpha = np.empty(self.config.alpha_shape, dtype=np.complex128)
        self.w_H = np.conjugate(self.w.T)

    def define_constants(self):
        self.x_i = np.linspace(0, 1, self.config.alpha_shape[0])  # Peseudo-data
        self.y_i = np.linspace(0, 1, self.config.alpha_shape[0])  # Peseudo-data
        self.theta_range = np.deg2rad(np.arange(0, 361, 1))  # Convert degrees to radians
        self.phi_range = np.deg2rad(np.arange(0, 91, 1))  # Convert degrees to radians

    @staticmethod
    def f(self, theta, phi):
        return np.ones(self.config.alpha_shape[0]) # Peseudo-data

    def compute_alpha(self):
        for i, theta in enumerate(self.theta_range):
            for j, phi in enumerate(self.phi_range):
                self.alpha[:, i, j] = self.f(self, theta, phi) * np.exp(
                    -1j * self.k0 * (self.x_i * np.sin(theta) * np.cos(phi) + self.y_i * np.sin(theta) * np.sin(phi))
                )

    def gradient_descent_optimization(self):
        for iteration in range(self.max_iterations):
            J_MV = 0
            gradient = np.zeros(self.w.shape, dtype=np.complex128)

            for theta in range(self.config.alpha_shape[1]):
                for phi in range(self.config.alpha_shape[2]):
                    alpha_slice = self.alpha[:, theta, phi].reshape(-1, 1)
                    F_theta_phi = np.dot(self.w_H, alpha_slice)
                    F_max = np.max(np.abs(F_theta_phi))
                    error = np.abs(F_theta_phi - self.F0[theta, phi] * np.exp(1j * np.angle(F_theta_phi) / F_max)) ** 2
                    J_MV += error

                    gradient += 2 * (F_theta_phi - self.F0[theta, phi] * np.exp(1j * np.angle(F_theta_phi) / F_max)) * np.conjugate(alpha_slice)

            self.w -= self.eta * gradient

            if iteration % 100 == 0:
                print(f"Iteration {iteration}, J_MV = {J_MV}")

    def run(self):
        self.compute_alpha()
        self.gradient_descent_optimization()
        print("Optimized weights w:")
        print(self.w)

def main():
    # Usage
    optimiser = GradientDescentoptimiser('config.yaml')
    optimiser.run()

if __name__ == '__main__':
    main()
