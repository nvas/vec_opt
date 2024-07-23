#!/usr/bin/env python3
"""
Author: Sajid Fadlelseed
Date: 2024-07-23
Description: This script performs gradient descent optimisation based on a specified configuration file.
It initializes variables, defines constants, and carries out the optimization process with parameters
specified in the configuration file.

Usage:
    python install_packages.py
"""

import ast
import subprocess
import sys
import pkg_resources

# Mapping for common package name discrepancies
PACKAGE_NAME_MAP = {
    'yaml': 'PyYAML',
    # Add more mappings if necessary
}

def get_imports_from_script(script_path):
    """Extract import statements from a Python script."""
    with open(script_path, 'r') as file:
        tree = ast.parse(file.read(), filename=script_path)
    
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    
    return imports

def install_packages(packages):
    """Install the given packages using pip."""
    for package in packages:
        # Use mapping if available
        package_name = PACKAGE_NAME_MAP.get(package, package)
        try:
            pkg_resources.require(package_name)
            # print(f"{package_name} is already installed.")
        except pkg_resources.DistributionNotFound:
            print(f"Installing {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

if __name__ == "__main__":
    # Path to the script you want to analyse
    script_path = 'optimiser.py'  # Replace with your script path
    
    # Extract imports
    packages = get_imports_from_script(script_path)
    
    # Install packages
    install_packages(packages)
