#!/usr/bin/env/python
import subprocess
import os

def main():
    while True:
     op = input(("Console: Enter 'help' for a list of options\n"))
     pop = op.split()
     print(pop)
     first = pop[0].lower()
     print(first)
     def choice():
       if first == "lg":
        os.system("lootGen.py ")
       elif first == "dx":
        os.system("rollD([pop[1]], [pop[2]])", shell=True)
       #elif first == "exit" or "q":
       # return
       else:
         print("Invalid Entry")

if __name__ == "__main__":
   main()