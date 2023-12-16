from pathlib import Path
import re

# Day 02, Advent of Code 2023

# regex string for game id
RE_GAME_ID  = re.compile(r'Game (\d+)')

# regex strings for color cubes
RE_RED      = re.compile(r'(\d+) red')
RE_BLUE     = re.compile(r'(\d+) blue')
RE_GREEN    = re.compile(r'(\d+) green')

# cube count parameters
RED_COUNT   = 12
BLUE_COUNT  = 14
GREEN_COUNT = 13


# main function
def main():
    # vars
    sum = 0

    # read through the input file
    with open(Path('input/day_02/input.txt'), 'r') as in_file:

        # read through each line
        for line in in_file:

            """ Code for Part 1

            # extract game id
            game_id     = int(re.match(RE_GAME_ID, line).group(1))
            """

            # extract all red counts and find the max
            red_max     = int(max(re.findall(RE_RED, line), key=int))

            """ Code for Part 1

            # if its an impossible amount skip this game
            if red_max > RED_COUNT:
                continue
            """

            # extract all blue counts and find the max
            blue_max    = int(max(re.findall(RE_BLUE, line), key=int))

            """ Code for Part 1

            # if its an impossible amount skip this game
            if blue_max > BLUE_COUNT:
                continue
            """

            # extract all green counts and find the max
            green_max   = int(max(re.findall(RE_GREEN, line), key=int))
            
            """ Code for Part 1

            # if its an impossible amount skip this game
            if green_max > GREEN_COUNT:
                continue

            # clearly its possible
            sum += game_id
            """

            """ Code for Part 2 """
            power = red_max * blue_max * green_max
            sum += power
            """ """

    """ Code for Part 1

    # print out the solution
    print(f'Sum of valid game ids: {sum}')
    """
    
    # print out the solution
    print(f'Sum of power: {sum}')

    return


if __name__ == '__main__':
    main()
