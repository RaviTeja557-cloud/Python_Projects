import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(choose[user_choice])
computer_choice=random.randint(1,2)
print("computer choose")
print(choose[computer_choice])
if user_choice<0 or user_choice>=3:
    print("you choose involed number")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you loose")
elif user_choice > computer_choice:
    print("use win")
elif computer_choice > user_choice:
    print("you loose")
elif computer_choice==user_choice:
    print("it is draw")
