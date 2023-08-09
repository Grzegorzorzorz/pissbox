#!/usr/bin/python

import sys

def main():
    user_input = ''
    for arg in range(1, len(sys.argv)):
        user_input = user_input + sys.argv[arg] + " "

    user_input = user_input[0:len(user_input) - 1]

    for char in user_input:
        sys.stdout.write(f"||{char}||")

    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
