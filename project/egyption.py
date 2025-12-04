is_egyption = input ("Are you Egyption? Type 'yes' or 'no' \n").lower()

if is_egyption == "yes":
    print("Good, that's the first step")
    is_18 = input ("Are you above 18? Type 'yes' or 'no' \n").lower()

    if is_18 == 'yes':
        print("You can have an ID")
    else :
        print("Sorry, you have to be 18 or older")
        print("Please try again when you are 18")

else :
    print("Sorry, an Egyption ID is give only to Egyptions")