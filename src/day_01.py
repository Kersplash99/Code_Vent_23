from pathlib import Path
import re

# Day 01, Advent of Code 2023

# converts input string to numeric digit
def to_numeric_digit( digit_str ):
    # this is a digit already ha!
    if digit_str.isdigit():
        return digit_str

    # there has to be a better way right?!!!
    match digit_str:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'

    # no luck why are we even here
    return None


# main function
def main():
    # vars
    sum = 0

    # read through the input file
    with open(Path('input/day_01/input.txt'), 'r') as in_file:

        # read through each line
        for line in in_file:

            # Code for Part 1
            """
            digit = ''

            # iterate through until we hit the first digit
            for c in line:
                if c.isdigit():
                    # store digit and index
                    digit = c
                    break

            # iterate backward until you hit the last digit
            for c in line[::-1]:
                if c.isdigit():
                    digit += c
                    break

            # sum += int(digit)
            """

            # Code for Part 2

            # find all the digits in the string and then get the value from first and last
            digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line.strip())
            calibration_val = to_numeric_digit(digits[0]) + to_numeric_digit(digits[-1])

            sum += int(calibration_val)
    
    # print out the total
    print(f'Total calibration value: {sum}')  
    return
    

if __name__ == '__main__':
    main()
