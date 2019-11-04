#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program adds positive integers


def main():
    # this function adds positive integers

    # variables
    answer = 0

    # input
    adding_number = int(input("Enter the amount of numbers you want to add: "))
    print("")

    # process & output
    for counter in range(adding_number):
        number_chosen = int(input("Enter a number to be added: "))
        if number_chosen < 0:
            continue

        else:
            answer = answer + number_chosen
            print("")
            print("The sum of all numbers is......", answer)
            print("")


if __name__ == "__main__":
    main()
