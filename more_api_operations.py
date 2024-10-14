#! import pandas and matplotlib for plotting and use pandas .methods() to plot and Data Frame operations.
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file using pandas and skip the first metadata row since first Data containst unneded info.
df = pd.read_csv("./index-holdings-xlf.csv", skiprows=1)

#! Convert 'Volume' column to string before using string operations, then convert it to pd.to_numeric method and pass in params. of DataFrame. errors="coerce"' will replace invalid parsings with NaN. errors <- is a error-handler.
df["Volume"] = pd.to_numeric(
    df["Volume"].astype(str).str.replace("M", "").str.replace(",", ""), errors="coerce"
)

# Ensure 'Last' column is numeric
df["Last"] = pd.to_numeric(df["Last"], errors="coerce")

# Plot the stock symbols against their 'Last' price, using the bar chart!
plt.figure(figsize=(10, 6))
df.plot(x="Symbol", y="Last", kind="bar", figsize=(12, 8), legend=False)
plt.title("Stock Prices of Different Companies index")
plt.xlabel("Stock Symbol")
plt.ylabel("Last Price")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Plot the stock symbols against their 'Volume' using the bar chart again!
plt.figure(figsize=(10, 6))
df.plot(x="Symbol", y="Volume", kind="bar", figsize=(12, 8), legend=False)
plt.title("Trading Volume of Different Companies")
plt.xlabel("Stock Symbol")
plt.ylabel("Volume (in millions)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Line plot of companies
plt.figure(figsize=(10, 6))
plt.plot(df["Symbol"], df["Last"], marker="o")
plt.title("Stock Prices of Different Companies using Line Plot")
plt.xlabel("Stock Symbol")
plt.ylabel("Last Price")
plt.xticks(ticks=range(len(df["Symbol"])), labels=df["Symbol"], rotation=90)
plt.tight_layout()
plt.show()

# Scatter plot for companies
plt.figure(figsize=(10, 6))
plt.scatter(df["Last"], df["Volume"])
plt.title("Scatter Plot: Last Price vs Trading Volume")
plt.xlabel("Last Price")
plt.ylabel("Trading Volume (in millions)")

# Loop to annotate each company on the plot for visualization (might be useful)
for i, symbol in enumerate(df["Symbol"]):
    plt.annotate(symbol, (df["Last"][i], df["Volume"][i]), fontsize=9, ha="right")
plt.tight_layout()
plt.show()

# Sort companies by highest volume and plot Top 5 companies by volume using the Bar Chart!
df_sorted_by_volume = df.sort_values(by="Volume", ascending=False)
plt.figure(figsize=(10, 6))
df_sorted_by_volume.head(5).plot(
    x="Symbol", y="Volume", kind="bar", figsize=(12, 8), legend=False
)
plt.title("Top 5 Companies by Trading Volume")
plt.xlabel("Stock Symbol")
plt.ylabel("Volume (in millions)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# Histogram individual data points are grouped into bins, it’s not possible to label each stock symbol directly
plt.figure(figsize=(10, 6))
df["Last"].plot(
    kind="hist", bins=20, figsize=(12, 8), color="orange", edgecolor="black"
)
plt.title("Distribution of Stock Prices (Last)")
plt.xlabel("Last Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


#! how many companies have corp in the company name

cond_corp = df["Company Name"].str.contains("Corp", case=False)
print(df[cond_corp].count()[0])


# Index weight of companies by largest! and their names!
df["Index Weight"] = pd.to_numeric(
    df["Index Weight"].astype(str).str.replace("%", ""), errors="coerce"
)

#! Sort companies by index weight and plot Top 5 companies by index weight using the Bar Chart! plt. method of matlotlib.pyplot
df_sorted_five_largest = df.sort_values(by="Index Weight", ascending=False)
plt.figure(figsize=(8, 6))
# pass in the params of the five largest companies by index weight. Grab the keys of params of plt.
# fixed and added a .pie method with params
df_sorted_five_largest.head(5).plot.pie(
    x="Symbol",
    y="Index Weight",
    figsize=(12, 8),
    legend=False,
)
# some labeling for readability otherwise you can not see them (x, y titles and main title)
# you can also rotate it but I did not include it here
plt.title("Top 5 Companies by Index Weight")
plt.xlabel("Stock Symbol")
plt.ylabel("Index weight")
plt.tight_layout()  # tight layout method of the plt. to adjust padding for better vis.
plt.show()

#! legend = false removes as an error checker againts the df. plt plot to see if there are any legends in the origional data set.

# Ensure 'Index Weight' is numeric by removing '%' and converting it to numeric
df["Index Weight"] = pd.to_numeric(
    df["Index Weight"].astype(str).str.replace("%", ""), errors="coerce"
)
# descending order ascending = False,
df_sorted_five_largest = df.sort_values(by="Index Weight", ascending=False).head(5)

# Create a pie chart for the top 5 companies by 'Index Weight' of the companies
plt.figure(figsize=(8, 6))
#! .pie method return a 'loop' kind of....
plt.pie(
    df_sorted_five_largest["Index Weight"],
    labels=df_sorted_five_largest["Company Name"],
    autopct="%1.1f%%",
    startangle=140,
)

plt.title("Top 5 Companies by Index Weight")
plt.tight_layout()
plt.show()

import pandas as pd

# Sample data with 'Volume' column containing strings with 'M' and 'K'
data = {"Volume": ["1.2M", "300K", "500M", "20K", "50"]}
df = pd.DataFrame(data)

# Convert 'Volume' to numeric using a lambda function
df["Volume"] = df["Volume"].apply(
    lambda x: (
        float(x.replace("M", "")) * 1_000_000
        if "M" in x
        else (float(x.replace("K", "")) * 1_000 if "K" in x else float(x))
    )
)

#! Print the converted DataFrame
print(df)

# Sample data for Volume and Last columns
data = {"Volume": ["1.2M", "300K", "500M", "20K", "50"], "Last": [90, 150, 120, 80, 60]}
df_sample = pd.DataFrame(data)

# Convert 'Volume' to numeric, handling the 'M' for millions (and 'K' for thousands if needed)
df_sample["Vol Lam"] = df_sample["Volume"].apply(
    lambda n: (
        float(n.replace("M", "")) * 1_000_000
        if "M" in n
        else float(n.replace("K", "")) * 1_000 if "K" in n else float(n)
    )
)

# Add 'Buy' or 'Sell' advice based on 'Last' price
df_sample["Advice"] = df_sample["Last"].apply(lambda n: "Buy" if n < 100 else "Sell")

# Print the DataFrame
print(df_sample)
