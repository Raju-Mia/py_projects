
import random
var = random.randint(1,5)
chance = 0
while True:
    if chance < 3:
        chance += 1
        var2 = int(input("inter the value: "))
        if var2 == var:
            print("Your guess is right!")
            break
        elif var2 < var:
            print("guess is bigger")
        elif var2 > var:
            print("guess is smaller ")
        else:
            print("try agian")
    else:
        print("ok")
        break

print("GMAE IS OVER.")