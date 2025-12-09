import random 

paper_ascii = '''
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            '''
rock_ascii ='''
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            '''
scissors_ascii= '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''

print("Welcome to the Rock, Paper, Scissors game:")
choice = input("Press Enter to continue or type (Help) for the rules: ").capitalize()
if choice == "Help":
    print("""
          ********** RULES *********** 
          1) You choose and the computer chooses
          2) Rock smashes Scissors -> Rock wins 
          3) Scissors cut Paper -> Scissors wins
          4) Paper covers Rock -> Paper wins 
""")
    
user_choise = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

if user_choise not in ["Rock","Paper","Scissors"]:
    print("Invalide chice! ")
elif user_choise == "Rock":
    print("\n You chose: \n",rock_ascii)
elif user_choise == "Paper":
    print("\n You chose: \n",paper_ascii)
elif user_choise == "Scissors":
    print("\n You chose: \n",scissors_ascii)

computer_choice = random.choice(["Rock","Paper","Scissors"])
if computer_choice == "Rock":
    print("\n Computer chose: \n",rock_ascii)
if computer_choice == "Paper":
    print("\n Computer chose: \n",paper_ascii)
if computer_choice == "Scissors":
    print("\n Computer chose: \n",scissors_ascii)
    
if user_choise == computer_choice:
    print("It's a tie!")
elif (user_choise == "Rock" and computer_choice == "Scissors" 
      or
      user_choise == "Paper" and computer_choice == "Rock"
      or 
      user_choise == "Scissors" and computer_choice == "Paper"):
    print("you win")
else:
    print("you lost!")