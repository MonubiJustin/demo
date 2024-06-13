import random
import names_database
import os

# Function to display account information
def display(account_info):
    name = account_info['name']
    description = account_info['description']
    country = account_info['country']
    return f'{name}, a {description}, from {country}.'


# Function to check if the user's guess is correct
def check_answer(guess, followers_count1, followers_count2):
    if followers_count1 > followers_count2:
        return guess == 1
    elif followers_count2 > followers_count1:
        return guess == 2


# Initialize the score
score = 0

# Pick the first account randomly
account_2 = random.choice(names_database.names)

# Continue flag for the game loop
continue_flag = True

while continue_flag:
    account_1 = account_2
    # Ensure the two accounts are different
    while account_1 == account_2:
        account_2 = random.choice(names_database.names)

    # Display the accounts to compare
    print(f'Compare 1: {display(account_1)}')
    print('\tvs\t')
    print(f'Compare 2: {display(account_2)}')

    # Get the user's guess
    guess = input('Who has more followers? 1 or 2: ')

    # Validate the input
    while guess not in ['1', '2']:
        print("Invalid input. Please enter 1 or 2.")
        guess = input('Who has more followers? 1 or 2: ')

    guess = int(guess)
    follower_count_1 = account_1['follower_count']
    follower_count_2 = account_2['follower_count']

    # Clear the console (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the guess is correct
    is_correct = check_answer(guess, follower_count_1, follower_count_2)
    if is_correct:
        score += 1
        print(f'You are right! Your score is: {score}')
    else:
        print(f'You are wrong. Your final score is: {score}')
        continue_flag = False
