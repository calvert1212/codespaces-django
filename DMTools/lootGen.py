import DMTools.textItemToArray as textItemToArray;
import random;

gpVal = int(input("Enter Loot GP Value: "))
dropC = int(input("Enter 1 in X drop chance: "))
goldP = 0

while (gpVal > 0):
    x = random.randint(1,dropC)
    if (x == 1):
        itemArray = textItemToArray.arrify('itemList.txt')
        randI = (random.choice(itemArray))
        itemGP = int(randI[1])
        if (itemGP <= gpVal):
            print(randI)
            gpVal -= itemGP
    else:
        x = random.randint(1, gpVal)
        goldP += random.randint(1, x)
        gpVal -= x
print(goldP)