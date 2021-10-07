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

import random
user_choice=int(input("What do you choose? 0 for rock,1 for paper,2 for scissors"))
if user_choice>2 or user_choice<0:
 print("Enter valid input")
 user_choice=int(input("What do you choose? 0 for rock,1 for paper,2 for scissors"))

dict={0:rock,1:paper,2:scissors}
print(dict[user_choice])

comp_choice=random.randint(0,2)
print(dict[comp_choice])

if user_choice==comp_choice:
  print("Draw")
elif user_choice==0 and comp_choice==1:
  print("Computer wins")
elif user_choice==0 and comp_choice==2:
  print("User wins")
elif user_choice==1 and comp_choice==2:
  print("Computer wins")
elif user_choice==1 and comp_choice==0:
  print("User wins")
elif user_choice==2 and comp_choice==0:
  print("Comp wins")
elif user_choice==2 and comp_choice==1:
  print("User wins")
