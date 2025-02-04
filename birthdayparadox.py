<<<<<<< HEAD
"""Monte Carlo simulation of Birthday Paradox"""

import datetime, random

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # Year of birthdays is unimportant so we set the same year
        # for all birthdays.
        startOfYear = datetime.date(2001, 1 , 1)

        # Get a random day
=======
"""Birthday Paradox simulation.
This program is a Monte Carlo experiment of the birthday paradox.
The birthday paradox is the surprising probability that people share
the same birthday in a group of people.
This program explores the probabilities that people share the same
birthday in a given size of a group"""

import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

>>>>>>> 157530391b176c15d60c1a98be8fa1b6e719ded5
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
<<<<<<< HEAD
    # Return date object that occurs more than once
=======
>>>>>>> 157530391b176c15d60c1a98be8fa1b6e719ded5
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
<<<<<<< HEAD
            
def main():
    print('''A Monte Carlo Simulation of the birthday paradox
which shows the surprisingly high probability that 2 people 
in a group share the same birthday.''')
    
    while True:
        print('How many birthdays shall I generate? (Max 100)')
        try:
            numbDays = int(input('> '))
        except ValueError:
            print('Not valid input. Input must be an integer')
            continue
        break
    print()

    print('Here are', numbDays, 'birthdays.')
    birthdays = getBirthdays(numbDays)
=======


def main():
    print('''Birthday Paradox
          This program is a Monte Carlo simulation to show that the odds
          of two people having the same birthday in a group of N people is
          surprisingly large.
          ''')

    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May','Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    while True:
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')

        if response.isdecimal() and (0 < int(response) < 101):
            numBDays = int(response)
            break

    print()

    print('Here are', numBDays, 'birthdays:')
    birthdays = getBirthdays(numBDays)
>>>>>>> 157530391b176c15d60c1a98be8fa1b6e719ded5
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
<<<<<<< HEAD
        print(f'{monthName} {birthday.day}', end='')
    print('\n\n')

    match = getMatch(birthdays)
    if match != None:
        print(f'Multiple people have a birthday on {MONTHS[match.month - 1]} {match.day}')
    else:
        print('There are no matching birthdays.')
    print()

=======
        dateText = f'{monthName} {birthday.day}'
        print(dateText, end='')
    print()
    print()

    match = getMatch(birthdays)

    print('In this simulation, ', end='')
    if match != None:
        monthName = MONTHS[match.month - 1]
        dateText = f'{monthName} {match.day}'
        print('multiple people have a birthday on', dateText)
    else:
        print('there are no matching birthdays.')
    print()

    print('Generating', numBDays, 'random birthdays 100,000 times...')
    input('Press Enter to begin...')

    print('Let\'s run another 100,000 simulations.')
    simMatch = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch += 1
    print('100,000 simulations run.')

    probability = round(simMatch / 100_000 * 100, 2)
    print('Out of 100,000 simulations of', numBDays, 'people, there was a')
    print('matching birthday in that group', simMatch, 'times. This means')
    print('that', numBDays, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')

>>>>>>> 157530391b176c15d60c1a98be8fa1b6e719ded5
if __name__ == "__main__":
    main()