import random

#Odd oe even?
while True:
    user_choice=input("choose between odd and even: ")
    if user_choice == "even":
        print("U chose: ", user_choice)
        print("Computer chose: odd")
        break

    elif user_choice == "odd":
        print("U chose: ", user_choice)
        print("Computer chose: even")
        
        break
    else:
        print("Value not accepted.")

#User_number
while True:
    try:
        user_number=int(input("choose a number: "))
        print("User number: ", user_number)
        break
    except:
        print("Value not accepted.")

#Computer_nubmer
computer_number=random.randint(0,10)
print("Computer chose: ",computer_number)

#Sum
sum = computer_number + user_number
print("the sum is: ", sum)

if (sum%2)==0:
    print("User won!")
else:
    print("Computer won!")