import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file using pandas
df = pd.read_csv('./index-holdings-xlf.csv', skiprows=1)  # Skip the first metadata row (since it is a title)

# Display the first few rows of the DataFrame head method by default returns 5 index. 
print("First few rows of the DataFrame:")
print(df.head())

# Check the column names to ensure correct plotting
print("\nColumn names in the DataFrame:")
print(df.columns)

# Plotting based on available columns, e.g., 'Symbol' and 'Last' (or other relevant columns)
# Ensure the columns exist before plotting
if 'Symbol' in df.columns and 'Last' in df.columns:
    # Convert 'Last' column to numeric, removing any potential non-numeric characters (like commas)
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')
    
    # Plotting the stock symbols against their 'Last' price
    df.plot(x='Symbol', y='Last', kind='bar', figsize=(10,6), legend=False)
    
    # Customizing the plot
    plt.title('Stock Prices of Different Symbols')
    plt.xlabel('Stock Symbol')
    plt.ylabel('Last Price')
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()
else:
    print("The required columns ('Symbol' and 'Last') do not exist in the DataFrame.")