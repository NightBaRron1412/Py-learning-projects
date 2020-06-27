from random import randint

print("""
	                    WELCOME TO AMIR'S FIRST PYTHON PROGRAMM !!

I'm gonna pick a random integer from 1 to 100, and you have to guess the number. The rules are:
 1. On your first turn, if your guess is
   * within 10 of the number, I'm gonna say "WARM!"
   * further than 10 away from the number, I'm gonna say "COLD!"
 2. On all subsequent turns, if a guess is
   * closer to the number than the previous guess I'm gonna say "WARMER!"
   * farther from the number than the previous guess, return "COLDER!"
 3. When your guess equals the number, I'm gonna tell you that you've guessed correctly and how many guesses it took!""")
ANOTHER_GAME = 'y'
while ANOTHER_GAME == 'y':
    PICKED_NUM = randint(1, 100)
    GUESSES = [0]
    while True:
        ENTERED_NUM = int(input('\nTry to guess my number :P  :'))
        GUESSES.append(ENTERED_NUM)
        if ENTERED_NUM < 1 or ENTERED_NUM > 100:
            print('OUT OF BOUNDS')
        elif abs(ENTERED_NUM - PICKED_NUM) <= 10:
            print('WARM!')
        else:
            print('COLD!')
        break

    while True:
        ENTERED_NUM = int(input('\nTry to guess my number :P  :'))
        GUESSES.append(ENTERED_NUM)
        if ENTERED_NUM < 1 or ENTERED_NUM > 100:
            print('OUT OF BOUNDS')
        elif GUESSES[-1] != PICKED_NUM:
            if abs(GUESSES[-1] - PICKED_NUM) > abs(GUESSES[-2] - PICKED_NUM):
                print('COLDER!')
            else:
                print('WARMER!')
        else:
            print('That\'s True !! \n it took you ' + str(len(GUESSES)) +' guesses to figure it out :P')
            break
    ANOTHER_GAME = input('Do you want to play another game? [y/n]: ')
else: print('Okay, GoodBye Bitch')
