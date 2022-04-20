import matplotlib.pyplot as plt
import numpy as np

A = plt.imread("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/master/images/southwing.png")

"""
print(type(A))
plt.imshow(A, cmap='gray');
print("Image array shape (pixels): {}".format(A.shape))
"""
G = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

n = len(G)
d = n//2

B = np.zeros(A.shape)


# Not sure what i and j would be in this calculation??
for i in range(1, B.shape[0]- 1):
    for j in range(1, B.shape[1]- 1):
        for k in range(n):
            for l in range(n):
                B[i][j] = G[k][l]*A[i-d+k][j-d+l]

plt.imshow(B, cmap='gray')


#cost complexity O(pq)