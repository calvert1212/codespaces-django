import random;
#rolls x dY dice, keeps adding new rolls until calc != 1

calc = 1
sum = 0
while calc == 1:
    nD = int(input("Enter Number of dice: "))
    dF = int(input("Enter number of die faces: "))
    while(nD > 0):
        sum += random.randint(1,dF)
        nD -= 1
    print(sum)
    calc = int(input("Enter 1 to add another roll, any other number to exit"))