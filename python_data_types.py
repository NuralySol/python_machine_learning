import numpy as np

# 1. Create a NumPy array
b = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# 2. Basic Information and Attributes
print("Shape:", b.shape)  # Shape
print("Data Type:", b.dtype)  # Data Type
print("Size:", b.size)  # Size
print("Number of Dimensions:", b.ndim)  # Dimensions

# 3. Indexing and Slicing
print("Element at [0, 0]:", b[0, 0])  # Indexing
print("First row:", b[0, :])  # Slicing - First row
print("Second column:", b[:, 1])  # Slicing - Second column

# 4. Mathematical Operations
print("Adding 10 to each element:\n", b + 10)  # Addition
print("Subtracting 5 from each element:\n", b - 5)  # Subtraction
print("Multiplying each element by 2:\n", b * 2)  # Multiplication
print("Dividing each element by 10:\n", b / 10)  # Division

# 5. Element-wise Operations between two arrays
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element-wise addition of two arrays:\n", b + c)  # Element-wise addition

# 6. Aggregate Functions
print("Sum of all elements:", np.sum(b))  # Sum
print("Row-wise sum:", np.sum(b, axis=1))  # Row-wise sum
print("Column-wise sum:", np.sum(b, axis=0))  # Column-wise sum
print("Mean of all elements:", np.mean(b))  # Mean
print("Max element:", np.max(b))  # Maximum
print("Min element:", np.min(b))  # Minimum
print("Standard Deviation:", np.std(b))  # Standard Deviation

# 7. Matrix Operations
print(
    "Matrix multiplication (dot product) with another array:\n", np.dot(b, c)
)  # Matrix multiplication
print("Transpose of the array:\n", np.transpose(b))  # Transpose

# 8. Reshaping and Resizing
print("Reshaping the array to 1x9:\n", b.reshape(1, 9))  # Reshaping
print("Flattening the array:\n", b.flatten())  # Flattening
print(
    "Concatenating a new row to the array:\n",
    np.concatenate((b, np.array([[100, 110, 120]])), axis=0),
)  # Concatenation

# 9. Broadcasting
print(
    "Broadcasting (adding a 1D array to a 2D array):\n", b + np.array([1, 2, 3])
)  # Broadcasting

# 10. Sorting and Searching
print("Row-wise sort:\n", np.sort(b, axis=1))  # Sorting
print("Unique elements in the array:", np.unique(b))  # Unique elements
print("Indices of elements greater than 50:\n", np.where(b > 50))  # Searching

# 11. Copying Arrays
# Shallow Copy
b_copy = b
b_copy[0, 0] = 99
print(
    "Original array after shallow copy modification:\n", b
)  # The original array is modified

# Deep Copy
b_deep_copy = b.copy()
b_deep_copy[0, 0] = 100
print(
    "Original array after deep copy modification:\n", b
)  # The original array remains unchanged



# •	Basic operations like checking shape, size, and type of the array.
# •	Indexing and slicing to access specific elements or rows/columns.
# •	Mathematical operations like addition, subtraction, multiplication, and division.
# •	Aggregate functions like sum, mean, max, min, and standard deviation.
# •	Matrix operations like matrix multiplication and transpose.
# •	Reshaping, flattening, and concatenation of arrays.
# •	Broadcasting to add arrays of different shapes.
# •	Sorting and searching in arrays.
# •	Shallow and deep copy to understand how modifying arrays works.
