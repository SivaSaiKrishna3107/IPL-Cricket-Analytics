import pandas as pd

# Load cleaned deliveries dataset
deliveries = pd.read_csv("data/deliveries_clean.csv")

# -------------------------------
# PLAYER COMPARISON
# -------------------------------

player_stats = deliveries.groupby("batter").agg(
    Runs=("batsman_runs", "sum"),
    Balls=("ball", "count"),
    Fours=("batsman_runs", lambda x: (x == 4).sum()),
    Sixes=("batsman_runs", lambda x: (x == 6).sum())
)

player_stats["Strike Rate"] = (
    player_stats["Runs"] / player_stats["Balls"] * 100
).round(2)

player_stats = player_stats.sort_values(
    by="Runs",
    ascending=False
)

player_stats.to_csv("data/player_comparison.csv")

print(player_stats.head(20))

print("\n✅ Player Comparison File Created Successfully!")