from bipolar import bipolar
import numpy as np
import matplotlib.pyplot as plt

# Example parameters
k = 5    # sparsity level
n = 20   # signal length

# Generate binary and bipolar matrices
A, B = bipolar(k, n)

# Display the results
print("Binary matrix A:")
print(A)

print("\nBipolar matrix B:")
print(B)

# Visualize the bipolar matrix
plt.imshow(B, cmap='bwr', aspect='auto')
plt.title("Bipolar Matrix B")
plt.colorbar()
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
