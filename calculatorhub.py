import os

print("""CALCULATOR HUB V1""")
print("""
[1] Age Calculator
[2] Addition Calculator""")

setup = input("[!]: ")

if setup == '1':
    os.startfile('agecalc.py')

if setup == '2':
    os.startfile('calculator.py')