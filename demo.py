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

# A bipolar (±1) matrix can be generated from a binary (0/1) matrix A as follows:

m, n = A.shape
ones = np.ones((m, n), dtype=A.dtype)   # matrix of ones with same shape as A
B = 2*A - ones                          # maps 0 -> -1 and 1 -> +1

# The bipolar matrix B satisfies the same RNSP order as A.
