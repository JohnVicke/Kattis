responses = ['too high', 'too low', 'right on']
upper_limit = 10
lower_limit = 1
out = ''

playing = True
while playing:
    guess = int(input())
    if guess == 0:
        print(out)
        exit()
    response = input()
    # High = 0, Low = 1, Correct = 2
    # If its too high
    if out != 'Stan is dishonest':
        if response == responses[0]:
            if guess >= upper_limit:
                out = 'Stan is dishonest'
                upper_limit = guess
            else:
                out = 'Stan may be honest'

        elif response == responses[1]:
            if guess <= lower_limit:
                out = 'Stan is dishonest'
            else:
                out = 'Stan may be honest'
                lower_limit = guess

    elif response == responses[2]:
        upper_limit = 10
        lower_limit = 1
        print(out)
        out = ''
