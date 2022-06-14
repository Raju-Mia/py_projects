import random
random_num = random.randint(1,10)
guess_num = None
while guess_num != "username":
    guess_num = input("Inter you guess Number 1 to 10 : ")
    new_guess_num = int(guess_num)
    if new_guess_num == random_num:
        print("Congatulation --- for ur lucky Number.")
        break
    else:
        print("Sorry Wrong Guess-try Again PlZ")