
#! import pandas and matplotlib for plotting and use pandas .methods() to plot and Data Frame operations. 
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file using pandas and skip the first metadata row since first Data containst unneded info.
df = pd.read_csv("./index-holdings-xlf.csv", skiprows=1)

# Convert 'Volume' column to string before using string operations, then convert it to pd.to_numeric method and pass in params. of DataFrame. 
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
