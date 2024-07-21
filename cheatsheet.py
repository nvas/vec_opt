import numpy as np

# =============================
# One-dimensional array slicing:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slice from index 2 to 5
slice1 = arr[2:6]  # Output: [2, 3, 4, 5]

# Slice from start to index 4
slice2 = arr[:5]  # Output: [0, 1, 2, 3, 4]

# Slice from index 5 to the end
slice3 = arr[5:]  # Output: [5, 6, 7, 8, 9]

# Slice with step
slice4 = arr[1:8:2]  # Output: [1, 3, 5, 7]

# Slice with negative index
slice5 = arr[-5:-2]  # Output: [5, 6, 7]
# =============================
# Two-dimensional array slicing:
arr2d = np.array([[0, 1, 2], 
                  [3, 4, 5], 
                  [6, 7, 8], 
                  [9, 10, 11]])

# Slice rows 1 and 2, and columns 1 and 2
slice1 = arr2d[1:3, 1:3]  # Output: [[4, 5], [7, 8]]

# Slice all rows for column 0
slice2 = arr2d[:, 0]  # Output: [0, 3, 6, 9]

# Slice first two rows for all columns
slice3 = arr2d[:2, :]  # Output: [[0, 1, 2], [3, 4, 5]]

# Slice last two columns for all rows
slice4 = arr2d[:, -2:]  # Output: [[1, 2], [4, 5], [7, 8], [10, 11]]
