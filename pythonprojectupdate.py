print("\nWelcome! Unsure what videogame to start next? I can help.\nJust follow the on-screen instructions and I will find the perfect game for you! \nLet's start with your name")

name = input("Please enter your name here: ")

print(f"\nHello {name}! \nAs some of our videogame suggestions are rated PEGI 18 \nI need you to confirm your age before you start \nIf you are under 18 this will terminate the programme.")

age = int(input("Please enter your age here: ")) 
year = 2022 - age

if year > 2004:
    print("\nSorry you are not old enough to play PEGI 18 games. \nThis particular programme is not for you. ")

elif year % 4 == 0 and year % 100 != 0:
    print("\n Did you know you were born in a leap year?! \nAnyway, we should probably get started. Just follow the instructions on the screen.")

elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("\n Did you know you were born in a leap year?! \nAnyway, we should probably get started. Just follow the instructions on the screen.")

else:
    print(f"\nI heard {year} was quite the year! \nAnyway, we should probably get started. Just follow the instructions on the screen.")

while True: 
    answer = input("\nWhat is your preferred game genre? \n\n1 = Horror \n2 = Action / Adventure   \n3 = Exit Programme \n\nEnter number here: ")
    if answer == "1":
        answer = input ("\nDo you want a zombie themed horror game? Enter yes or no here: ")
        if answer == "yes":
            answer = input ("\nDo you want the game to be multiplayer? Enter yes or no here: ")
            if answer == "yes":
                print("\nI would reccommend: \n\nLeft4Dead \nBack4Blood \n7DaystoDie")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")
                    break
                elif answer == "no":
                    print("\n\n\nI'm sorry to hear that - follow the instructions on screen to try again :) ")
                else:
                    print("\nPlease enter yes or no. You have been returned to the main menu.")
            elif answer == "no":
                print("\nI would reccommend: \n\nDead Island \nLast of Us \nDying Light")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")
                    break
                elif answer == "no":
                    print("\n\n\nI;m sorry to hear that - follow the instructions on screen to try again :)")
                else:
                    print("\nPlease enter yes or no. You have been returned to the main menu.")
            else:
                print("\nplease enter yes or no. You have been returned to the main menu.")
        elif answer == "no":
            print("\nI would reccommend: \n\nOutlast \nFive Night's at Freddies \nP.T.")
            answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
            if answer == "yes":
                print("\nAmazing! Bye :)")
                break
            elif answer == "no":
                print("\n\n\nI;m sorry to hear that - follow the instructions on screen to try again :)")
            else:
                print("\nPlease enter yes or no. You have been returned to the main menu.")
        else:
            print("\n\nplease enter yes or no. You have been returned to the main menu.")
    elif answer == "2":
        answer = input("\nDo you want the game to be open world? Enter yes or no here: ")
        if answer == "yes":
            answer = input("\nDo you want the game to be set in a dystopian or furturistic world? Enter yes or no here: ")
            if answer == "yes":
                print("\nI would reccomnend: \n\nFallout4 \nArk Survival Evolved")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")
                    break
                if answer == "no":
                    print ("\n\n\nI;m sorry to hear that - follow the instructions on screen to try again :)")
                else:
                    print("\n\nPlease enter yes or no. You have been returned to the main menu.")
            elif answer == "no":
                print("\nI would reccommend: \n\nRed Dead Redemption 2 \nGTA 5 \nFar Cry 6")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")
                    break
                if answer == "no":
                    print("\n\n\nI;m sorry to hear that - follow the instructions on screen to try again :)")
                else:
                    print("\n\nPlease enter yes or no. You have been returned to the main menu.")
            else:
                print("\n\nPlease enter yes or no. You have been returned to the main menu.")
        elif answer == "no":
            answer = input ("\nDo you want the game to have a dark and edgy feel? Enter yes or no here: ")
            if answer == "yes":
                print("\nI would reccommend: \n\nVampyre \nDishonoured 2")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")
                    break
                if answer == "no":
                    print ("\n\n\nI;m sorry to hear that - follow the instructions on screen to try again :)")    
            elif answer == "no":
                print("\nI would reccommend: \n\nElder Scrolls Skyrim \nWitcher 3 \nLost Kingdoms 2")
                answer = input ("\nAre you happy with your suggestions? \nEnter yes to exit or no to start again: ")
                if answer == "yes":
                    print("\nAmazing! Bye :)")  
                    break  
                if answer == "no": 
                    print ("\n\n\nI'm sorry to hear that - follow the instructions on screen to try again :)")
            else:
                print("\n\nPlease enter yes or no. You have been returned to the main menu.")
        else:
            print("\n\nPlease enter yes or no.  You have been returned to the main menu.")
   
    elif answer == "3":
        print("\nGoodbye")
        break 
    else:
        print("\n\n\nPlease enter 1, 2 or 3")
        