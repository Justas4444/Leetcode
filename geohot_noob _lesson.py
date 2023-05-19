import numpy as np

N=5

if __name__ == "__main__":
    A = np.random.randn(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)
    C = A @ B
    print(C)