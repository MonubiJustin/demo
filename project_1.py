import os
import random

import names_database
score = 0

def display(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"
def check_answer(guess, follower_count1, follower_count2):
    if follower_count1 > follower_count2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False
account_2 = random.choice(names_database.names)
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(names_database.names)
    while account_1 == account_2:
        account_2 = random.choice(names_database.names)
    print(f"Compare 1: {display(account_1)}")
    print('\t\t\t\t\t\tvs')
    print(f"Compare 2: {display(account_2)}")
    guess = int(input("Who has more followers? type 1 or 2:"))
    followers_count_1 = account_1['follower_count']
    followers_count_2 = account_2['follower_count']
    os.system('cls')
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    if is_correct == True:
        score += 1
        print(f"You are right. Your score is: {score}")
    else:
        print(f"You are wrong. Your score is: {score}")
        continue_flag = False
