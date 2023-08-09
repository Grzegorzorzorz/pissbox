#!/usr/bin/env python

import sys


def main():
    arse = []
    if len(sys.argv) < 3:
        arse.append(input("She... "))
        arse.append(input("on my... "))
        arse.append(input("until I... "))
    else:
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            arse.append(arg)

    print(f"She {arse[0]} on my {arse[1]} until I {arse[2]}.")


if __name__ == '__main__':
    main()
