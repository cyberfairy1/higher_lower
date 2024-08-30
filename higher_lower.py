from higher_lower_art import logo, vs  # type: ignore
from game_data import data # type: ignore
import random
import os 

# Format account data into printable format.
# It's easier just to create a function, because you have to call it for both accounts
def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}.")

## If Statement - turned into a function
def check_answer(guess, a_followers, b_followers):
    '''Take the user guess and follower counts and returns if they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Now you can call clear_screen() whenever you want to clear the screen.

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make game repeatable.
while game_should_continue:
    # Generate a random account from the game data.
    
    # Make account at position B become the next account at position A.
    account_a = account_b
    
    if account_a == account_b:
        account_b = random.choice(data)
   
    # Here we are calling the function from above 
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_folower_count = account_b["follower_count"]

    is_correct= check_answer(guess, a_follower_count, b_folower_count)
    
    # Clear screen between rounds.
    clear_screen()
    print(logo)

    # Give user feedback on their guess.
    # Score Keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

