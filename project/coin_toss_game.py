import random 

print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")
choose = int(input("Enter your choice (1 or 2):"))


if choose == 1:
    if random.random() >= 0.5:
        computer_result = "Heads"
    else :
        computer_result = "Tails"
elif choose == 2 :
    if  random.randint(0,1)== 1 :
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print("Ivaild choice")
    exit()
    
choice = input("Enter your Guess (Heads or Tails): ").lower()

if choice != computer_result.lower():
    print("Sorry, you lost!")
    print("The computer's coin toss result was:",computer_result)
elif choice == computer_result.lower():
    print("Congratoliton! you win.")
    print("The computer's coin toss result was :",computer_result)