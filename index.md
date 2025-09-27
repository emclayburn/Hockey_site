---
title: Ethan's github page
---

<!-- Include MathJax for LaTeX rendering -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# Analyzing Blues Player Statistics using Python
 This is a site dedicated to hockey statistics, most specifically the **St. Louis Blues**

# About The Blues
The **St. Louis Blues** are a professional hockey team located in St. Louis Missouri. The team came into existence in 1967, being one of six new teams added. They have one Stanley Cup win, coming in 2019. After a first round exit in 2025, they gear up for a new season starting October 9th against the **Minnesota Wild**.

<p align="center">
  <img src="images/St._Louis_Blues_logo.svg" alt="St. Louis Blues Logo" width="200">
</p>

## Blues Players Backgrounds
In the game of hockey, points by a player is one of the most important things. A point is described as either a goal or an assist. The more points a player has, generally the better they are. During the 2024-25 season, **Robert Thomas** led the club in points with 81.

<div style="text-align: center;">
  <img src="images/Robert_Thomas.png" alt="Bob Thomas" width="150">
</div>

Robert Thomas racked up 81 points in 70 games, but only 21 were goals, highlighting his role as the team’s primary playmaker. His top targets? Jordan Kyrou and Pavel Buchnevich, each receiving 9 of his assists. Thomas excels at creating high-danger chances, making him indispensable for the Blues’ top line. This is not a surprise since this trio was the top line for St. Louis during the 24-25 season. This will likely change this season with **Kyrou** being swapped out of the top line for **Jimmy Snuggerud**.

## Thomas Analysis

What makes a center important? Is it the assists? Is it the goals? What can we do to measure Robert Thomas's worth on the team? For now, lets check out Robert Thomas's goals, assists, and exoected goals with him shooting. For this, we are going to load data gathered from MoneyPuck.com: [Skater Data](https://moneypuck.com/data.htm) Scroll down to skaters and download the 2024-2025 file. Using this data, we can do analysis and see Thomas's production.

```python
import pandas as pd

# Read your CSV file from your "data" folder
df = pd.read_csv("data/skaters.csv")

# Filter for Robert Thomas
thomas_df = df[df["name"] == "Robert Thomas"]

# Keep only the columns you care about
tidy_df = thomas_df[["games_played", "situation", "icetime", "shifts", "I_F_xGoals", "I_F_goals", "I_F_primaryAssists", "I_F_points", "OnIce_F_xGoals"]]

# Preview the tidy DataFrame
print(tidy_df)

# Optional: save to Markdown for your GitHub Pages
tidy_df.to_markdown("thomas.md")
```

Inputing the code without tidying it up will result in a lot more data than we are interested in. When we run this chunk in python, we will get this chart

## Preview of Data

| name           | team | position | situation | games_played | icetime | xGoals | goals | primaryAssists | secondaryAssists | points | onIce_xGoals |
|----------------|------|---------|-----------|--------------|---------|--------|-------|----------------|-----------------|--------|--------------|
| Robert Thomas  | STL  | C       | other     | 70           | 5335    | 2.84   | 7     | 5              | 3               | 15     | 16.66        |
| Robert Thomas  | STL  | C       | all       | 70           | 83824   | 16.88  | 21    | 35             | 25              | 81     | 86.99        |
| Robert Thomas  | STL  | C       | 5on5      | 70           | 63798   | 12.14  | 12    | 19             | 17              | 48     | 51.59        |
| Robert Thomas  | STL  | C       | 4on5      | 70           | 5399    | 0.32   | 1     | 0              | 0               | 1      | 1.03         |
| Robert Thomas  | STL  | C       | 5on4      | 70           | 9292    | 1.50   | 1     | 11             | 5               | 17     | 17.56        |

### Goals vs Expected Goals
If we want to chart the data, we can use this function

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/skaters.csv")
thomas = df[df["name"] == "Robert Thomas"]

# Bar chart of goals vs xGoals
bar = thomas.plot.bar(x="situation", y=["I_F_goals", "I_F_xGoals"])

bar.set_title("Robert Thomas: Goals vs Expected Goals")
bar.set_xlabel("Situation")
bar.set_ylabel("Number of goals")

for p in bar.patches:
    height = round(p.get_height())  # Round the value
    bar.annotate(f'{height}',
                (p.get_x() + p.get_width() / 2, height + 0.1),  # Slightly above bar
                ha='center', va='bottom')

# Save figure
plt.tight_layout()

plt.savefig("images/thomas_goals.png")
```
![Robert Thomas Goals](images/thomas_goals.png)

## So what?

Looking at this data, we can see that Robert Thomas is a higher goal scorer than expected. Robert Thomas isn't just any center, he's the engine of the Blues' top line, facilitating plays, setting up teammates, and creating scoring chances as a high rate. If you want to do this analysis for your favorite players, just replace Robert Thomas with their name, such as Quinn Hughes!

# Further Analysis

The goalie for the Blues is **Jordan Binnington**. He came into the spotlight in 2019 leading the Blues to the Stanley Cup win. 

<div style="text-align: center;">
  <img src="images/Binnington.png" alt="Jordan Binnington" width="400">
</div>

Many fans in hockey don't know if **Binnington** is a good goalie or not. Some people think that he is flashy, but doesn't perform that great all the time. How can we tell if he is a good goalie or not? Are there numbers to back up either way? Of course there is, lets dive in.

# Important Statistics
What are some stats that would be key in showing the effectiveness of a goalie? Maybe you want to see the total goals that have given up, maybe goals per game, maybe even goals per 60 minutes, 

$$
\text{G/60} = \frac{\text{Goals Allowed}}{\text{Ice Time (minutes)}} \times 60
$$

 or save percentage,

 $$
\text{SV\%} = \frac{\text{Shots Faced} - \text{Goals Allowed}}{\text{Shots Faced}}
$$

 These could all be good indicators to whether a goalie is good or not. What we are going to do for this example is load in an excel file of all goalie information from the 24-25 season and see how effective **Binnington** truly was. A link to download the file is found here on the MoneyPuck.com website, as they are the ones that collected the data: [Goalie Data](https://moneypuck.com/data.htm). Scroll down to goalies and download the 2024-2025 file.

To read an Excel file in Python using pandas:

```python
import pandas as pd
# Read your CSV file from your "data" folder
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

```
Inputing the code without tidying it up will result in a lot more data than we are interested in. When we run this chunk in python, we will get this chart

## Preview of Data

| name | team | position | situation | games_played | icetime | xGoals | goals |
|------|------|---------|-----------|--------------|---------|--------|-------|
| Jordan Binnington | STL | G | other | 56 | 4316 | 11.5 | 13 |
| Jordan Binnington | STL | G | all   | 56 | 194339 | 150.25 | 145 |
| Jordan Binnington | STL | G | 5on5  | 56 | 165286 | 105.17 | 100 |
| Jordan Binnington | STL | G | 4on5  | 56 | 13295 | 30.45 | 30 |
| Jordan Binnington | STL | G | 5on4  | 56 | 11442 | 1.97  | 1 |

### Goals vs Expected Goals
If we want to chart the data, we can use this function
```python
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
```


![Jordan Binnington Goals](images/binnington_goals.png)

## So what?
What conclusions can we draw from this data? From this data we can see that in every situation listed like 5 on 5 or on a 5 on 4 powerplay, **Jordan Binnington** lets up less goals than is expected of him. The only situations where he gives up more than expected is in the other situations, like up 5 on 3 or down 3 to 5. For a goalie, that is a really good thing, stoping more shots than expected. 

One of the best parts about this analysis is that you can look at any goalie in the data set. If you wanted to see how good **Joel Hofer**, the Blue backup goalie, is compared to Binnington, you just need to replace Jordan Binnington with Joel Hofer and it will compute for you. 