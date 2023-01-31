#!/usr/bin/env python3

import sys

with open("fileprocessor.input","w") as file1:

    sys.stdout = file1

    for i in file1:
        print(i)
    sys.stdout = sys.stdout
    
file1.close()
