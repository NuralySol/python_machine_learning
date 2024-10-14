import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file using pandas and skip the first metadata row
df = pd.read_csv("./index-holdings-xlf.csv", skiprows=1)

# Display information about the DataFrame
df.info()

# Check for missing values
print("\nMissing values per column:")
print(df.isna().sum())

# Remove the percentage sign (%) from the "Index Weight" column and convert it to float
if "Index Weight" in df.columns:
    df["Index Weight"] = df["Index Weight"].str.strip("%").astype(float)

# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())

# Check the column names to ensure correct plotting
print("\nColumn names in the DataFrame:")
print(df.columns)

# Ensure 'Symbol' and 'Last' columns exist before plotting
if "Symbol" in df.columns and "Last" in df.columns:
    # Convert 'Last' column to numeric, removing any potential non-numeric characters (like commas)
    df["Last"] = pd.to_numeric(df["Last"], errors="coerce")

    # Plot the stock symbols against their 'Last' price
    df.plot(x="Symbol", y="Last", kind="bar", figsize=(10, 6), legend=False)

    # Customizing the plot
    plt.title("Stock Prices of Different Symbols")
    plt.xlabel("Stock Symbol")
    plt.ylabel("Last Price")
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()
else:
    print("The required columns ('Symbol' and 'Last') do not exist in the DataFrame.")

# Ensure 'Volume' column is numeric by removing non-numeric characters ('M' for millions, commas)
df["Volume"] = pd.to_numeric(df["Volume"].str.replace("M", "").str.replace(",", ""), errors="coerce")

# Calculate and print total volume
total_volume = df["Volume"].sum()
print("Total Volume:", total_volume)

# Filter stocks with prices less than 100 using different methods

# 1. Using .query() method
stocks_below_100_query = df.query("Last < 100")

# 2. Using .loc[] method
stocks_below_100_loc = df.loc[df["Last"] < 100]

# 3. Using .filter() method (to filter columns, not rows)
filtered_columns = df.filter(items=["Symbol", "Last"])
stocks_below_100_filtered = filtered_columns.loc[filtered_columns["Last"] < 100]

# Display the results from different filtering methods
print("Stocks with prices less than 100 (using .query()):")
print(stocks_below_100_query)

print("\nStocks with prices less than 100 (using .loc()):")
print(stocks_below_100_loc)

print("\nFiltered stock symbols and prices less than 100 (using .filter() and .loc()):")
print(stocks_below_100_filtered)

# Retrieve the last price of the company with symbol 'C' using .loc[] and .query() methods

# Using .loc[] method
df["Last"] = pd.to_numeric(df["Last"], errors="coerce")
last_price_C_loc = df.loc[df["Symbol"] == "C", "Last"].values[0]
print(f"Last price of the company with symbol 'C' (using .loc()): {last_price_C_loc}")

# Using .query() method
last_price_C_query = df.query('Symbol == "C"')["Last"].values[0]
print(f"Last price of the company with symbol 'C' (using .query()): {last_price_C_query}")

# Sort by highest volume and display top 5 companies with the largest volume
df_sorted_by_volume = df.sort_values(by="Volume", ascending=False)
print("\nTop 5 companies with the highest volume:")
print(df_sorted_by_volume[["Symbol", "Volume"]].head())


#! Summary of the above operations.
#   1.	Reading the CSV:
# 	•	The script reads a CSV file containing stock data using pandas.read_csv(), skipping metadata rows to focus on the relevant data.
# 	2.	Handling Missing Values:
# 	•	The script checks for missing values in the DataFrame using df.isna().sum() and displays the results.
# 	3.	Cleaning the Data:
# 	•	For the Index Weight column, it strips the percentage sign (%) and converts the values to float.
# 	•	The Volume column, which may contain commas and the letter “M” (for millions), is cleaned by removing these non-numeric characters and converting the values to float using pd.to_numeric().
# 	4.	Plotting Stock Prices:
# 	•	The script checks if both the Symbol and Last columns exist, then plots the stock symbols (on the x-axis) against their respective Last prices (on the y-axis) using matplotlib.
# 	•	It customizes the plot by rotating the x-axis labels for readability.
# 	5.	Calculating Total Volume:
# 	•	After cleaning the Volume column, the script calculates the total trading volume across all stocks using df["Volume"].sum() and displays the result.
# 	6.	Filtering Stocks Below a Certain Price:
# 	•	The script filters stocks where the Last price is less than 100 using three different methods:
# 	•	Using .query(): Queries the DataFrame for stocks with prices below 100.
# 	•	Using .loc[]: Filters rows based on the condition that the Last price is less than 100.
# 	•	Using .filter(): Selects specific columns (Symbol, Last) and filters for prices below 100.
# 	7.	Retrieving the Last Price of a Specific Company:
# 	•	The script retrieves the Last price of the company with the symbol 'C' using two methods:
# 	•	Using .loc[]: Locates the row where the symbol is 'C' and extracts the Last price.
# 	•	Using .query(): Queries the DataFrame to find the stock with symbol 'C' and retrieves the Last price.
# 	8.	Sorting by Trading Volume:
# 	•	The companies are sorted based on their Volume in descending order, and the top 5 companies with the highest trading volume are displayed.
