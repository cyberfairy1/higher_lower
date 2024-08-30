from higher_lower_art import logo, vs  
from game_data import data
import random
import os 

# Formats the account details into a more presentable format.
def format_data(account):
    '''Takes account info and returns a snappy, printable format.'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

# Checks if the player's guess is correct.
def check_answer(guess, a_followers, b_followers):
    '''Compares user guess to actual follower counts and returns if they're on point.'''
    return (guess == "a" and a_followers > b_followers) or (guess == "b" and b_followers > a_followers)

# Clears the terminal screen.
def clear_screen():
    """Wipes the screen clean, ready for the next round."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Start the game with some flair!
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# The main game loop, keeps going as long as the player is correct.
while game_should_continue:
    # Move account B to account A's position for the next round.
    account_a = account_b
    account_b = random.choice(data)

    # Ensure that the next account isn't the same as the previous.
    while account_a == account_b:
        account_b = random.choice(data)
   
    # Present the two accounts to the player.
    print(f"Challenger A: {format_data(account_a)}")
    print(vs)
    print(f"Challenger B: {format_data(account_b)}")
    
    # Get the player's guess.
    guess = input("Who’s got more followers? Type 'A' or 'B': ").lower()

    # Check if the player guessed right.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the screen to build suspense.
    clear_screen()
    print(logo)

    # Give feedback on the guess and update the score.
    if is_correct:
        score += 1
        print(f"Boom! You’re right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Oof, that’s a miss! Final score: {score}")
