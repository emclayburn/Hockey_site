import pandas as pd

# Read your CSV file
df = pd.read_csv("data/goalies.csv")

# Filter for Jordan Binnington
binnington_df = df[df["name"] == "Jordan Binnington"]

# Preview his rows
print(binnington_df)

# Optional: save to Markdown for your GitHub Pages
binnington_df.to_markdown("binnington.md")