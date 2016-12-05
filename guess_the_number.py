import random

N0_OF_GUESSES = 10
RANGE_TOP = 10
BEGIN = random.randint(0, 10)
guesses_left = 10
while True:
    # generate the random number
    random_number = random.randint(BEGIN, RANGE_TOP)

    # give the user a certain amount of guesses
    for i in range(N0_OF_GUESSES):
        guess = int(raw_input('guess the number between ' + str(BEGIN) + ' and ' + str(RANGE_TOP) + ': '))
        guesses_left -= 1
        print "you have " + str(guesses_left) + " guesses left."
       # if guesses_left > 0 or guesses_left < 11:
            if guess == random_number:
                print 'well done'
                break
            elif guess > random_number:
                print "too high"
            else:
                print "too low"

    print "let's try a new number!"

#print "Guess a number between " + str(BEGIN) + " and " + str(RANGE_TOP)