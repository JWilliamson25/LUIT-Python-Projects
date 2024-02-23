#!/bin/python3

import math
import os
import random
import re
import sys


  # Input: A single line containing a positive integer, n.
n = int(input().strip())

# Constraints: 1 <= n <= 100
if not 1 <= n <= 100:
    print("Number out of bounds")
else:
    # Conditional actions
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")      