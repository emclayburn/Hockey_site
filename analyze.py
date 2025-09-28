# Jordan Binnington Stats
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

# Robert Thomas Stats
import pandas as pd

df = pd.read_csv("data/skaters.csv")

thomas_df = df[df["name"] == "Robert Thomas"]

tidy_df = thomas_df[["games_played", "situation", "icetime", "shifts", "I_F_xGoals", "I_F_goals", "I_F_primaryAssists","I_F_secondaryAssists", "I_F_points"]]

print(tidy_df)

tidy_df.to_markdown("thomas.md")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/skaters.csv")
thomas = df[df["name"] == "Robert Thomas"]

# Bar chart of goals vs xGoals
bar = thomas.plot.bar(x="situation", y=["I_F_goals", "I_F_xGoals"])

bar.set_title("Robert Thomas: Goals vs Expected Goals")
bar.set_xlabel("Situation")
bar.set_ylabel("Number of goals")
bar.legend(["Goals", "Expected Goals"])

for p in bar.patches:
    height = round(p.get_height())  # Round the value
    bar.annotate(f'{height}',
                (p.get_x() + p.get_width() / 2, height + 0.1),  # Slightly above bar
                ha='center', va='bottom')

# Save figure
plt.tight_layout()

plt.savefig("images/thomas_goals.png")