import pandas as pd

# Load Excel
df = pd.read_excel("data/goalies.csv")

# Get summary stats
summary = df.describe()

# Save a small preview for Markdown
df.head(10).to_markdown("preview.md")   # first 10 rows
summary.to_markdown("summary.md")       # summary stats