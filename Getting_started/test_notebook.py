import pandas as pd
import matplotlib.pyplot as plt


CARD = ["heart", "club", "spade", "diamond"]

def compute_vals(df: pd.DataFrame, card: list, target_col: str, team_col: str):
	for i in range(len(card)):
		df_team = df[df[team_col] == card[i]]
		av_hour = df_team[target_col].mean()
		min_hour = df_team[target_col].min()
		max_hour = df_team[target_col].max()
		print(f"The average hours of sleep for team {card[i]} is {av_hour}")
		print(f"The minimum hours of sleep for team {card[i]} is {min_hour}")
		print(f"The maximum hours of sleep for team {card[i]} is {max_hour}")
		print()

# compute_vals(data, COLOR_CARD, "sleep_hour", "card_col")

def visualize_fav_season(df: pd.DataFrame, card: list, target_col: str, 
						 nrow: int = 1, ncol: int = 2):
	
	_, axes = plt.subplots(nrow, ncol, figsize=(16, 12), sharex=True)
	for i, team in enumerate(card):     # team: heart
		team_df = df[df["card_col"] == team]
		x_axis = list(dict(team_df[target_col].value_counts()).keys())
		y_axis = list(dict(team_df[target_col].value_counts()).values())
		axes[i].bar(x_axis, y_axis)
		axes[i].set_ylabel('Number of students')
		axes[i].set_title(f"Favorite seasons in team {team}")
		axes[i].legend(title='Favorite seasons')

	plt.title("Favorite seasons in each team")
	plt.show()