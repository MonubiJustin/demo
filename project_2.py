import random
import names_database
import os
score = 0
def display(account_info):
    name = account_info['name']
    description = account_info['description']
    country = account_info['country']
    return f'{name}, a {description}, from {country}.'
def check_answer(guess, followers_count1, followers_count2):
    if followers_count1 > followers_count2:
        if guess == 1:
            return True
        else:
            return False
    elif followers_count2 > followers_count1:
        if guess == 2:
            return True
        else:
            return False



account_2 = random.choice(names_database.names)

continue_flag = True
while continue_flag:
    account_1 = account_2
    while account_1 == account_2:
        account_2 = random.choice(names_database.names)
    print(f'Compare 1: {display(account_1)}')

    print('\tvs\t')

    print(f'Compare 2: {display(account_2)}')
    guess = int(input('Who has more followers? 1 or 2: '))
    follower_count_1 = account_1['follower_count']
    follower_count_2 = account_2['follower_count']
    os.system('cls')
    is_correct = check_answer(guess, follower_count_1, follower_count_2)
    if is_correct:
        score += 1
        print(f'You are right. Your score is: {score}')
    else:
        print(f'You are wrong. your score is: {score}')
        continue_flag = False

