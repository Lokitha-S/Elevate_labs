import numpy as np
def task():
    arr_1d = np.array([1, 2, 3])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"1D Array Shape: {arr_1d.shape}")
    print(f"2D Array Shape: {arr_2d.shape}")

    squared = np.square(arr_1d)
    added = arr_1d + 10

    broadcast_result = arr_2d + arr_1d
    print("Broadcasting of 2d & 1d:",broadcast_result)

    print(f"Mean: {np.mean(arr_2d)}")
    print(f"Standard Deviation: {np.std(arr_2d)}")
    print(f"Sum across rows: {np.sum(arr_2d, axis=1)}")

    size = 1000000
    p_list = list(range(size))
    n_array = np.arange(size)

    random_matrix = np.random.rand(3, 3)
    optimized = np.exp(arr_1d)

    print("\nVisualization")
    print(f"Matrix:\n{random_matrix}")
    print(f"Dimensions: {random_matrix.ndim}, Size: {random_matrix.size}, Type: {random_matrix.dtype}")

if __name__ == "__main__":
    task()