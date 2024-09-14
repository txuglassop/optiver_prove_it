import random

def simulate_game():
    total_sum = 0
    current_player = 1 
    while True:
        roll = random.randint(1, 6) 
        total_sum += roll 
        if total_sum >= 6:
            return current_player, total_sum
        
        # switch turns
        current_player = 2 if current_player == 1 else 1

def simulate_games(num_simulations):
    total_payoff_p1 = 0 
    total_payoff_p2 = 0 

    for _ in range(num_simulations):
        winner, payoff = simulate_game()
        if winner == 1:
            total_payoff_p1 += payoff
        else:
            total_payoff_p2 += payoff

    # return expected values
    expected_value_p1 = total_payoff_p1 / num_simulations
    expected_value_p2 = total_payoff_p2 / num_simulations

    return expected_value_p1, expected_value_p2

num_simulations = 1000000000
ev_p1, ev_p2 = simulate_games(num_simulations)
print(f"Simulated EV for Player 1: {ev_p1:.4f}")
print(f"Simulated EV for Player 2: {ev_p2:.4f}")
