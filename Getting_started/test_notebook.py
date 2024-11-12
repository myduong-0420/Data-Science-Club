import pandas as pd
import matplotlib.pyplot as plt

def compute_vals(df: pd.DataFrame, card: list, target_col: str, team_col: str, target_print: str = "hours of sleep"):
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
        print(f"The average {target_print} for team {card[i]} is {av_hour}")
        print(f"The minimum {target_print} for team {card[i]} is {min_hour}")
        print(f"The maximum {target_print} for team {card[i]} is {max_hour}")
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
    team_col (str): The column name representing the teams.
    nrow (int, optional): The number of rows in the subplot grid. Default is 1.
    ncol (int, optional): The number of columns in the subplot grid. Default is 2.

    """
    all_seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    _, axes = plt.subplots(nrow, ncol, figsize=(16, 4*nrow), sharex=True)
    axes = axes.flatten()

    for i, team in enumerate(card):
        team_df = df[df[team_col] == team]

        season_counts = team_df[target_col].value_counts().reindex(all_seasons, fill_value=0)
        x_axis = season_counts.index.tolist()  # Fixed set of seasons
        y_axis = season_counts.values.tolist()  # Corresponding counts
        bar_colors = ['forestgreen', 'gold', 'coral', 'darkturquoise']

        # Create bar plot
        bars = axes[i].bar(x_axis, y_axis, color=bar_colors)
        axes[i].set_ylabel('Number of students')
        axes[i].set_title(f"Favorite seasons in team {team}")

        # Set legend using x_axis as labels
        axes[i].legend(bars, x_axis, title='Favorite seasons')

    plt.suptitle("Favorite seasons in each team", fontsize=20)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
    plt.show()


def visualize(df: pd.DataFrame, card: list, target_col: str, team_col: str,
                       nrow: int = 1, ncol: int = 2, subtitle="Fear proportion in team", title: str = "Illustration of college fear"):
    """
    Visualizes the proportion of fears for each team using pie charts.

    Parameters:
    df (pd.DataFrame): The input dataframe containing the data.
    card (list): A list of unique team identifiers to filter the dataframe.
    target_col (str): The column name in the dataframe representing the fear category.
    team_col (str): The column name representing the teams.
    nrow (int, optional): The number of rows in the subplot grid. Default is 1.
    ncol (int, optional): The number of columns in the subplot grid. Default is 2.

    """
    _, axes = plt.subplots(nrow, ncol, figsize=(16, 6*nrow), sharex=True)
    axes = axes.flatten()

    for i, team in enumerate(card):
        team_df = df[df[team_col] == team]
        labels = list(dict(team_df[target_col].value_counts()).keys())
        x = list(dict(team_df[target_col].value_counts()).values())
        axes[i].pie(x, labels=labels, autopct='%1.1f%%')
        axes[i].set_title(f"{subtitle} {team}")

    plt.suptitle(title)
    plt.show()

from collections import Counter

from collections import Counter

def findMaximumTasks(task, m):
    # Step 1: Count the frequency of each task
    task_count = Counter(task)
    
    # Step 2: Convert the frequencies into a sorted list
    frequencies = list(task_count.values())
    frequencies.sort(reverse=True)
    
    # Step 3: Greedily distribute tasks to maximize unique task sets
    total_unique_tasks = 0
    sets = [0] * m  # Array to keep track of how many tasks each node processes
    
    # Distribute the tasks as long as there are tasks left and nodes can take more
    while frequencies:
        for i in range(m):
            if frequencies and frequencies[0] > 0:  # Assign task to node i
                sets[i] += 1  # Assign one task to node i
                frequencies[0] -= 1  # Decrease frequency of the most frequent task
                
                # Re-sort the frequency array to maintain highest-first order
                frequencies.sort(reverse=True)
                
                # Increase the total unique tasks processed
                total_unique_tasks += 1
                
            # If frequencies[0] becomes 0, we pop it from the list
            if frequencies and frequencies[0] == 0:
                frequencies.pop(0)
    
    return total_unique_tasks

# Example usage
task = [1, 2, 2, 1, 3, 1, 3]
m = 2
print(findMaximumTasks(task, m))  # Output: Maximum number of unique tasks processed
