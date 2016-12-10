import random

N0_OF_GUESSES = 10
RANGE_TOP = 10


while True:
    # generate the random number
    BEGIN = random.randint(0, 4)
    random_number = random.randint(BEGIN, RANGE_TOP)
    
    # give the user a certain amount of guesses
    #for i in reversed(range(N0_OF_GUESSES)):
    for i in range(N0_OF_GUESSES)[::-1]:
        guess = int(raw_input('guess the number between ' + str(BEGIN) + ' and ' + str(RANGE_TOP) + ': '))

        print "you have " + str(i) + " guesses left."

        if guess == random_number:
            print 'well done'
            break
        elif guess > random_number:
            print "too high"
        else:
            print "too low"

    print "let's try a new number!"