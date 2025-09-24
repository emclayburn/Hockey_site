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
bar = binnington.plot.bar(x="situation", y=["goals", "xGoals"])

bar.set_title("Jordan Binnington: Goals vs Expected Goals")
bar.set_xlabel("Situation")
bar.set_ylabel("Number of goals")

for p in bar.patches:
    height = round(p.get_height())  # Round the value
    bar.annotate(f'{height}',
                (p.get_x() + p.get_width() / 2, height + 0.1),  # Slightly above bar
                ha='center', va='bottom')

# Save figure
plt.tight_layout()

plt.savefig("images/binnington_goals.png")