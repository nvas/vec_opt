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




def parse_arguments():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description='This script performs gradient descent optimisation based on a specified configuration file. '
                    'It initialises variables, defines constants, and carries out the optimisation process '
                    'with dimensions specified in the configuration file.'
    )
    return parser.parse_args()



def main(args):



    # Load configuration
    opt = optimiser.GradientDescentoptimiser('config.yaml')

    # Run optimisation
    opt.run()

if __name__ == '__main__':
    
    # Parse arguments
    args = parse_arguments()
    
    # Call the main function with parsed arguments
    main(args)