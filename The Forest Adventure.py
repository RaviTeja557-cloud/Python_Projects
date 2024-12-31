print('''You find yourself in a mysterious forest. The air is cool, and the sound of birds echoes around you. 
      In front of you are two paths.''')
choice_1=input("One leads to the towering mountains in the distance.while the other disappears into the darkness of a cave.(mountains/cave)").lower()
if choice_1=="mountains":
    print("You climb higher and higher until you find an ancient temple.")
    choice_2=input("Inside the temple are two doors: one made of gold and the other of silver. Which will you choose?").lower()
    if choice_2=="gold":
        print("You enter a room filled with treasure. Congratulations, you’ve won!")
    elif choice_2=="silver":
        print("The moment you step inside, magical chains bind you. You’re trapped forever.")
    else:
        print("You made an invalid choice. Game over!")
elif choice_1=="cave":
    print("The path grows darker with every step, and suddenly, you hear a growl. A shadowy creature blocks your way.")
    choice_3=input("Do you fight or run?").lower()
    if choice_3=="fight":
        print("a treasure chest sparkles in the dim light. You’ve found the hidden treasure!")
    elif choice_3=="run":
        print("You escape back to the forest, but the treasure remains undiscovered.")
    else:
        print("You made an invalid choice. Game over!")
else:
    print("You made an invalid choice. Game over!")