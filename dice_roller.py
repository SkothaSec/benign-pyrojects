import random

#start function
def main():
    print('''
        What dice would you like to roll?
        type HELP for available commands
        type QUIT to exit program''')
    user_options()

def user_options():
    while True:
        user_input = input('''
        Choose your dice!
        > ''')
        if user_input.lower() == "help":
            print('''
            Type "QUIT" to exit the program
            the Dice format is as follows:
            roll 2D8
            will print the results of rolling 2, 8 sided die.
            Format: <amount of dice to roll>D<how many sides the die should have>''')
        elif user_input == "quit":
            print("thank's for rolling!")
            exit()
        else:
            user_roll(user_input)


def user_roll(user_input):
        user_input = user_input.lower().split("d")
        user_input = int(user_input[0]), int(user_input[1])
        count = user_input[0]
        faces = user_input[1]
        print("you rolled " + str(count) + ', ' + str(faces) + ' sided dice')
        roll_list = []
        for number in range(1, count + 1):
            roll = random.randint(1, faces)
            roll_list.append(roll)
            print("roll", number, "landed: ", roll)
        print("total value of rolls: ", sum(roll_list))
main()