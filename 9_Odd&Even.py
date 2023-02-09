import random

#Odd or even?
while True:
    user_choice=input("choose between odd and even: ")
    if user_choice == "even":
        print("U chose: ", user_choice)
        print(" ")
        break

    elif user_choice == "odd":
        print("U chose: ", user_choice)
        print(" ")
        break

    else:
        print("Value not accepted.")

#User_number
while True:
    try:
        user_number=int(input("User number: "))
        break
    except:
        print("Value not accepted.")

#Computer_nubmer
computer_number=random.randint(0,10)
print("Computer number: ",computer_number)

#Sum
sum = computer_number + user_number
print(" ")
print("the sum is: ", sum)

if (sum%2)==0:
    print("User won!")
    print(" ")
else:
    print("Computer won!")
    print(" ")