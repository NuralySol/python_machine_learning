# Import necessary libraries
import pandas as pd
import numpy as np

# Notes about data types and libraries
# String is a sequential data type, wrapped in quotes. It is immutable (cannot be changed).
# In Python, we can use functions like `type()`, `dir()`, and `help()` to explore objects and data types.
# Immutable types (like strings, tuples) can be used as dictionary keys.
# A library is a collection of functions and methods.
# A tuple, being immutable, can also be used as a key in a dictionary.

# Create a list of numbers
num = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
num_array = np.array(num)

# Add 5 to each element of the array (element-wise operation)
result = num_array + 5

# Print the NumPy array and the result of the addition
print("Original NumPy Array:", num_array)
print("Result after adding 5 to each element:", result)

# Creating a 2D list
b = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# Convert the list to a NumPy array
b = np.array(b)

# Now you can proceed with your operations
print("Shape of the array:", b.shape)  # Output: (3, 3)
print("First element in the array:", b[0, 0])  # Output: 10 (first element)
print("Last element in the array:", b[2, 2])  # Output: 90 (last element)

# Element-wise operations
print(
    "Array after adding 10:\n", b + 10
)  # Output: [[20, 30, 40], [50, 60, 70], [80, 90, 100]]
print(
    "Array after subtracting 5:\n", b - 5
)  # Output: [[5, 15, 25], [35, 45, 55], [65, 75, 85]]
print(
    "Array after multiplying by 2:\n", b * 2
)  # Output: [[20, 40, 60], [80, 100, 120], [140, 160, 180]]
print(
    "Array after dividing by 10:\n", b / 10
)  # Output: [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

# Create another array for element-wise operations
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Element-wise addition between arrays
print(
    "Element-wise addition with another array:\n", b + c
)  # Output: [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

# Aggregate function: Sum of all elements in the array
print("Sum of all elements in the array:", np.sum(b))  # Output: 450

# Additional useful NumPy operations for data science
print("Number of dimensions:", b.ndim)
print("Data type of the array:", b.dtype)
print("Shape of the array:", b.shape)

# Copying arrays (deep copy)
deep_copy_b = b.copy()

# Modifying the deep copy and checking if the original is unaffected
deep_copy_b[0, 0] = 100
print("Deep copy after modification:\n", deep_copy_b)
print("Original array remains unchanged:\n", b)

# Shallow copy (the default behavior without using .copy())
shallow_copy_b = b
shallow_copy_b[0, 0] = 99
print("Shallow copy modification affects original array:\n", b)

# ----------- Pandas Series Example --------------- #

# Create a Pandas Series from a list
data = [100, 200, 300, 400, 500]
index = ["a", "b", "c", "d", "e"]

series = pd.Series(data, index=index)
print("\nPandas Series:\n", series)

# Perform operations on the Series
print("\nSeries after adding 10:\n", series + 10)  # Adds 10 to each element

# Accessing a specific element in Series
print("\nAccessing element 'c' in Series:", series["c"])  # Output: 300

# Series with automatic integer index
series2 = pd.Series([5, 10, 15, 20, 25])
print("\nPandas Series with default integer index:\n", series2)

# Perform element-wise addition between two Series
print("\nElement-wise addition between two Series:\n", series + series2[:5])

# Create a simple DataFrame with some data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Occupation": ["Engineer", "Doctor", "Artist", "Lawyer"],
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Access specific columns
print("\nAccess the 'Name' column:")
print(df["Name"])

# Access rows using .loc (row label-based indexing)
print("\nAccess the row with index 1 (Bob's data):")
print(df.loc[1])

# Add a new column
df["Salary"] = [70000, 80000, 60000, 90000]
print("\nDataFrame after adding a new column 'Salary':")
print(df)

# Filtering rows (e.g., people older than 30)
filtered_df = df[df["Age"] > 30]
print("\nFilter rows where Age > 30:")
print(filtered_df)


# 1.	Creating a DataFrame: We created a DataFrame from a dictionary where keys are column names and values are lists of data.
# 2.	Accessing a Column: We accessed a specific column (Name) using df['Name'].
# 3.	Accessing a Row: We used .loc[] to access a specific row based on its index.
# 4.	Adding a Column: We added a new column (Salary) to the DataFrame.
# 5.	Filtering Data: We filtered the DataFrame to include only rows where Age > 30.




