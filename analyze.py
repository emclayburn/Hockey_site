import pandas as pd
# Read your CSV file
df = pd.read_csv("data/goalies.csv")

# Filter for Jordan Binnington
binnington_df = df[df["name"] == "Jordan Binnington"]

# Keep only the columns you care about
# Example: "team", "position", "games_played", "goals", "xGoals"
tidy_df = binnington_df[["games_played", "situation", "icetime", "goals", "xGoals"]]

# Preview the tidy DataFrame
print(tidy_df)

# Optional: save to Markdown for your GitHub Pages
tidy_df.to_markdown("binnington.md")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/goalies.csv")
binnington = df[df["name"] == "Jordan Binnington"]

# Bar chart of goals vs xGoals
binnington.plot.bar(x="situation", y=["goals", "xGoals"])
plt.savefig("images/binnington_goals.png")