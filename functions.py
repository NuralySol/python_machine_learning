import pandas as pd


# Define a function using def
def add(a, b):
    total = a + b
    return total


# Call the function and print the result
result = add(5, 6)
print("Result from add function:", result)

# Define a function using a lambda expression
f = lambda a, b: a + b


def is_even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


#! check the function with user input and intify it before processing since input is 'string' even the numbers!
user_input = int(input("Please input a number: "))
# call the function.
result = is_even_or_odd(user_input)
# print using the f - string
print(f"The number {user_input} is {result}.")

# Lambda function to return True if even, False if odd
is_even_or_odd = lambda number: True if number % 2 == 0 else False

# Get input from the user
user_input = int(input("Please input a number: "))

# Call the lambda function
result = is_even_or_odd(user_input)

# Print whether the number is even or odd based on the boolean result
if result:
    print(f"The number {user_input} is Even.")
else:
    print(f"The number {user_input} is Odd.")

#! never ever use a for loop in a DataFrame.

df = pd.DataFrame(
    list(range(1, 11)), columns=["Numbers"]
)  #! range is exclusive of the last 'range'
df["Greater than 5"] = df["Numbers"].apply(
    lambda number: number * 100 if number > 5 else number
)
print(df)

