#Randomly Generates Loot
import DMTools.textItemToArray as textItemToArray;
import random;

gpVal = int()
goldP = 0

def rollLoot(gpVal, dropC):
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
