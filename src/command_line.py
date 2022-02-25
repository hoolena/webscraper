# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import argparse

parser = argparse.ArgumentParser("This is a test")
parser.add_argument("-n", type=str, help="Argument to add your name")
parser.add_argument("-a", type=str, help="Argument to add your age")
parser.add_argument("-o", type=str, help="Argument to add your occupation")
args = parser.parse_args()
print("Your name is:", args.n)
print("Your age is:", args.a)
print("Your occupation is:", args.o)