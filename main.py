#!/usr/bin/env python3
"""
Author: Sajid Fadlelseed
Date: 2024-07-23
Description: This script runs the optimiser based on the dimensions providedi the config.yaml file.

Usage:
    python main.py
"""

import argparse
import optimiser
import subprocess



def parse_arguments():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description='This script performs gradient descent optimisation based on a specified configuration file. '
                    'It initialises variables, defines constants, and carries out the optimisation process '
                    'with dimensions specified in the configuration file.'
    )
    return parser.parse_args()


def run_installation_script():
    """Run the installation script with the provided path."""
    try:
        result = subprocess.run(
            ['python', '-W', 'ignore::DeprecationWarning', 'install_packages.py'],
            check=True,  # This will raise an exception if the command fails
            text=True    # This ensures the output is captured as a string
        )
        # print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the installation script.")
        print("Error message:", e.stderr)

def main(args):

    # Install missing packages
    run_installation_script()

    # Load configuration
    opt = optimiser.GradientDescentoptimiser('config.yaml')

    # Run optimisation
    opt.run()

if __name__ == '__main__':
    # Parse arguments
    args = parse_arguments()
    
    # Call the main function with parsed arguments
    main(args)