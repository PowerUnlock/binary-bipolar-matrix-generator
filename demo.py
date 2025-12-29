from bipolar import bipolar
import numpy as np
import matplotlib.pyplot as plt

# Example parameters
k = 5    # sparsity level
n = 20   # signal length

# Generate binary matrices
A = bipolar(k, n)

# Display the results
print("Binary matrix A:")
print(A)

