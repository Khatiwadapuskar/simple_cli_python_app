import random


def get_guess():
    """ gets user guess"""
    return list(input('What is your guess?  '))


def gen_computer_num():
    '''generates random 3-digit number'''
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def get_clues(gen_code, user_guess):
    ''' gets clues comparing user guess and generated number '''
    if gen_code == user_guess:
        return ['CODE CRACKED!!!', ]

    clues = []

    for ind, num in enumerate(user_guess):
        if num == gen_code[ind]:
            clues.append('Match!!')
        elif num in gen_code:
            clues.append('Close!!')

    if clues == []:
        return ['Nope!!', ]
    else:
        return clues


print('Welcome Number Cracker')

secret_num = gen_computer_num()

clue_report = []

while clue_report != 'CODE CRACKED!!!':
    guess = get_guess()

    clue_report = get_clues(secret_num, guess)

    print("Here's your result:  ")
    for clue in clue_report:
        print(clue)
