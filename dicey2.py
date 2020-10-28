# roll a die some number of times
import random
import sys

number_dice = 1

def roll_once(min, max):
    return random.randint(min, max)

def do_loop(number_dice):
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        for i in range(0, number_dice):
            print(roll_once(1,6))

        roll_again = input("Roll the dices again?")

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

def get_argument():
    if (len(sys.argv) == 1):
        return 1
    elif (len(sys.argv) == 2):
        return int(sys.argv[1])

def main():
    number_dice = get_argument()
    do_loop(number_dice)

main()
