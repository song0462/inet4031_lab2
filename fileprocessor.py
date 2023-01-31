#!/usr/bin/env python3

file1 = open("fileprocessor.input")
filecpy = file1.read()
print(filecpy)

filecpy = filecpy.split(":")
file1.close()
print("The list is: ", filecpy)
