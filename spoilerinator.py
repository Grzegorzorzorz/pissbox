#!/usr/bin/python

import sys

base_str = input()

for char in base_str:
    sys.stdout.write(f"||{char}||")

sys.stdout.write("\n")
