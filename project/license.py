age = int(input("How old are you? \n"))
license = input("You have license? choose (Yes),or (no)\n")
if age >= 18 and license.lower() == "yes":
    print("You can drive")
elif age < 18 or  license.lower() == "no":
    print("Sorry, You can't drive")
else:
    print("Sorry, your enter of [",license,"] is not understood")