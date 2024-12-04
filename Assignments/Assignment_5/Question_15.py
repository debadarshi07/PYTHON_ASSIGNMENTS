from random import randint

def roll_dice():
    return randint(1, 6) + randint(1, 6)

def play_game():
    point = 0
    roll_count = 1
    first_roll = roll_dice()
    if first_roll in [7, 11]:
        return {roll_count: 1}, {roll_count: 0}
    elif first_roll in [2, 3, 12]:
        return {roll_count: 0}, {roll_count: 1}
    point = first_roll
    while True:
        roll_count += 1
        roll = roll_dice()
        if roll == point:
            return {roll_count: 1}, {roll_count: 0}
        elif roll == 7:
            return {roll_count: 0}, {roll_count: 1}

def simulate_craps(num_games=1000000):
    wins = {}
    losses = {}
    total_wins = 0
    total_losses = 0
    for _ in range(num_games):
        game_wins, game_losses = play_game()
        total_wins += sum(game_wins.values())
        total_losses += sum(game_losses.values())
        for roll in game_wins:
            wins[roll] = wins.get(roll, 0) + game_wins[roll]
        for roll in game_losses:
            losses[roll] = losses.get(roll, 0) + game_losses[roll]
    return wins, losses, total_wins, total_losses, num_games

def display_results(wins, losses, total_wins, total_losses, num_games):
    total_rolls = max(max(wins.keys(), default=0), max(losses.keys(), default=0))
    print(f"Percentage of wins: {total_wins / num_games * 100:.1f}%")
    print(f"Percentage of losses: {total_losses / num_games * 100:.1f}%")
    print("\nPercentage of wins/losses based on total number of rolls:")
    print("Rolls | % Resolved on this roll | Cumulative % of games resolved")
    print("-" * 66)
    cumulative_resolved = 0
    for roll in range(1, total_rolls + 1):
        resolved_on_roll = wins.get(roll, 0) + losses.get(roll, 0)
        cumulative_resolved += resolved_on_roll
        if cumulative_resolved > 0:
            percent_resolved = resolved_on_roll / num_games * 100
            cumulative_percent = cumulative_resolved / num_games * 100
            print(f"{roll:5} | {percent_resolved:19.2f}% | {cumulative_percent:23.2f}%")

wins, losses, total_wins, total_losses, num_games = simulate_craps()
display_results(wins, losses, total_wins, total_losses, num_games)