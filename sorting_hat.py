# -----------------------------------------------------------------------------
# PROJECT: Hogwarts Sorting Hat
# DESCRIPTION: An interactive text-based game that sorts users into houses based 
#              on their personality choices and random chance.
# KEY CONCEPTS: User Input, Conditional Logic (If/Elif/Else), Random Modules.
# -----------------------------------------------------------------------------

import random

welc_msg = "Welcome to Hogwarts! Come forward and I will put the sorting hat on your head. Answer these questions truthfully and the sorting hat will do the rest.\nLie your way through these questions and you will be sent to the dungeons with the rest of the muggles!\nThe numbers is the game, the sorting hat is not to blame! Let the sorting begin!"
print(welc_msg)

q_1 = int(input("I wonder..Do you rise at Dawn or do you hide at Dusk? \n 1. Dawn \n 2. Dusk \n Enter your answer: "))
print(q_1)

if q_1 == 1:
  print("So you are a morning Hippogriff eh?!")

elif q_1 == 2:
  print("So you are a night Owl, do you not like to dream?")

else: 
  msg_1 = ("You are a muggle!")
  print(msg_1)

q_2 = int(input("Interesting and tell me this..When you are gone from the wizarding world, what would you want people to remember you as? \n 1. The Good \n 2. The Great \n 3. The Wise \n 4. The Bold \n Tell me quickly: "))
print(q_2)

if q_2 == 1:
  print("Your heart is as good as gold!")

elif q_2 == 2:
  print("I see all the mountains your want to climb in your future!")

elif q_2 == 3:
  print("You are already wise but still have a lot to learn!")

elif q_2 == 4:
  print("You have courage but be careful to look before you jump!")

else:
  print("You are a muggle!")

q_3 = int(input("Which class are you most excited to attend? \n 1. Transfiguration \n 2. Defence Against the Dark Arts \n 3. Potions \n 4. Herbology \n What will it be?"))
print(q_3)

if q_3 == 1:
  print("Very interesting..you belong to..")

elif q_3 == 2:
  print("Very interesting..you belong to..")

elif q_3 == 3:
  print("Very interesting..you belong to..")

elif q_3 == 4:
  print("Very interesting..you belong to..")

else:
  print("You are a muggle!")

random_number = random.randint(1, 5)

if random_number == 1:
  print("Gryfindor! A new lion has been added to the pride!")

elif random_number == 2:
  print("Ravenclaw! A new eagle has joined the flock!")

elif random_number == 3:
  print("Hufflepuff! A new badger has joined the burrow!") 

elif random_number == 4:
  print("Slytherin! A new snake has slithered into the dark!") 

else:
  print("A muggle has come to Hogwarts! Straight to the dungeons with you!")
