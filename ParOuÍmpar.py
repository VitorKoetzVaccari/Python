import random
import time

#Odd oe even?
while True:
    user_choice=input("Choose between odd and even: ")
    if user_choice == "even":
        print("\nYou ("+ user_choice + ") x "+ "Computer (Odd)")
        break
    elif user_choice == "odd":
        print("\nYou ("+ user_choice + ") x "+ "Computer (Even)")
        break
    else:
        print("\nValue not accepted. Try again.")

#User_number
while True:
    try:
        user_number=int(input("\nChoose a number: "))
        print("\nUser number: ", user_number)
        break
    except:
        print("\nValue not accepted.")

#Computer_nubmer
computer_number=random.randint(0,10)
print("\nComputer chose: ",computer_number)

#Sum
sum = computer_number + user_number
print("\nThe sum is: ", sum)

if (sum%2)==0:
    print("\nUser won!")
else:
    print("\nComputer won!")

time.sleep(200)
