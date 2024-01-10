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

#Write your code below this line 👇
#asking for prompt for the game
print("Welcome to the Rock, Paper & Scissor Game!\nPlease select 0 for Rock, 1 for Paper and 2 for Scissor.")

#getting the user's choice
person_choice = int(input("What's your choice?:"))

#print(type(person_choice)) checking the type

#generating a choice of the computer
computer_choice = random.randint(0,2)

#Printing out the choices
elements = [rock,paper,scissors]
print(f'Your selection:\n{elements[person_choice]}')
print(f'Computer selected:\n{elements[computer_choice]}')


#building logic
if person_choice==0 and computer_choice==2:
  print("Decision: You win")
elif person_choice==1 and computer_choice==0:
  print("Decision: You win")
elif person_choice==2 and computer_choice==1:
  print("Decision: You win")
else:
  if person_choice==computer_choice:
    print("No one wins! Play Again")
  else:
    print("Decision: Computer wins")
  
  

