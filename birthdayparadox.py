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
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    # Return date object that occurs more than once
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
            
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
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        print(f'{monthName} {birthday.day}', end='')
    print('\n\n')

    match = getMatch(birthdays)
    if match != None:
        print(f'Multiple people have a birthday on {MONTHS[match.month - 1]} {match.day}')
    else:
        print('There are no matching birthdays.')
    print()

if __name__ == "__main__":
    main()