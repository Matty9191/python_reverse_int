#!/usr/bin/env python


def reverse_int(num):
    '''
      Purpose: Reverse an integer passed as argument zero.
      Arguments: Argument 0 contains an integer to reverse
      Return values: Returns the reversed number or 0
    '''
    if type(num) != int:
        return("0")

    # Handles zero or a NULL value
    elif not num or num == 0:
        return("0")

    # Handles negative numbers
    elif num < 0:
        reverse = "-" + str(abs(num))[::-1]
        return(reverse)

    # Handles positive integers and numbers with leading zeros
    elif num > 0:
        return(str(num)[::-1].lstrip("0"))


def main():
    pass


if __name__ == "__main__":
    main()
