print("""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
""")


print("Welcome to my island!")
print("There are two doors in front of you.🚪a red door and 🚪a blue door")
choice = input("Which door do you want to open?\n").lower()
if choice == "red":
    print("Great! now you entered a room.")
    print("you found three boxes: 🎁 while, 🎁 black, 🎁 green")
    choice = input("Which box do you open?\n").lower()
    if choice == "green":
        print("Congratulations! You found the treasure! 💰💰💰")
    elif choice == "while":
        print("Oops! You opened a box filled with snakes 🐍🐍🐍")
        print("Game over! ")
    elif choice == "black":
        print("Oops! you opened a box filled with spiders 🕷️🕷️🕷️")
        print("Game over! ")
    else:
        print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
elif choice == "blue":
    print("Oops! You chose the crocodile door.")
    print("Game over! 🐊🐊🐊")
else:
    print("Invalid choice! 🤷‍♂️🤷‍♂️")