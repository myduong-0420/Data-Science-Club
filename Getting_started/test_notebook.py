import pandas as pd
import matplotlib.pyplot as plt


CARD = ["heart", "club", "spade", "diamond"]

def compute_vals(df: pd.DataFrame, card: list, target_col: str, team_col: str):
	"""
	Computes and prints the average, minimum, and maximum values of a target column for each team.

    Parameters:
    df (pd.DataFrame): The input dataframe containing the data.
    card (list): A list of unique team identifiers to filter the dataframe.
    target_col (str): The column name in the dataframe representing the target variable (e.g., hours of sleep).
    team_col (str): The column name in the dataframe representing the team identifier.

	"""
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

def visualize_fav_season(df: pd.DataFrame, card: list, target_col: str, team_col: str, 
                         nrow: int = 1, ncol: int = 2):
	"""
	Visualizes the distribution of favorite seasons for each team in a bar chart.

    Parameters:
    df (pd.DataFrame): The input dataframe containing the data.
    card (list): A list of unique team identifiers to filter the dataframe.
    target_col (str): The column name in the dataframe representing the favorite season.
    nrow (int, optional): The number of rows in the subplot grid. Default is 1.
    ncol (int, optional): The number of columns in the subplot grid. Default is 2.

	"""
    # Define all possible seasons
	all_seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	
	_, axes = plt.subplots(nrow, ncol, figsize=(16, 12), sharex=True)
	axes = axes.flatten()
	
	for i, team in enumerate(card):
		team_df = df[df[team_col] == team]
        
        # Get the counts of each season, ensuring all seasons are represented
		season_counts = team_df[target_col].value_counts().reindex(all_seasons, fill_value=0)
		x_axis = season_counts.index.tolist()  # Fixed set of seasons
		y_axis = season_counts.values.tolist()  # Corresponding counts
		bar_colors = ['red', 'pink', 'coral', 'orange']
        
        # Create bar plot
		bars = axes[i].bar(x_axis, y_axis, color=bar_colors)
		axes[i].set_ylabel('Number of students')
		axes[i].set_title(f"Favorite seasons in team {team}")
        
        # Set legend using x_axis as labels
		axes[i].legend(bars, x_axis, title='Favorite seasons')
	
	plt.suptitle("Favorite seasons in each team", fontsize=20)
	plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
	plt.show()


def visualize_big_fear(df: pd.DataFrame, card: list, target_col: str, team_col: str,
						 nrow: int = 1, ncol: int = 2):
	"""
	Visualizes the proportion of fears for each team using pie charts.

    Parameters:
    df (pd.DataFrame): The input dataframe containing the data.
    card (list): A list of unique team identifiers to filter the dataframe.
    target_col (str): The column name in the dataframe representing the fear category.
    nrow (int, optional): The number of rows in the subplot grid. Default is 1.
    ncol (int, optional): The number of columns in the subplot grid. Default is 2.

	"""
	_, axes = plt.subplots(nrow, ncol, figsize=(16, 12), sharex=True)
	axes = axes.flatten()

	for i, team in enumerate(card):     # team: heart
		team_df = df[df[team_col] == team]
		labels = list(dict(team_df[target_col].value_counts()).keys())
		x = list(dict(team_df[target_col].value_counts()).values())
		axes[i].pie(x, labels=labels, autopct='%1.1f%%')
		axes[i].set_title(f"Fear proportion in team {team}")

	plt.title("Illustration of college fear at today's event")
	plt.show()