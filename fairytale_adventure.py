# -----------------------------------------------------------------------------
# PROJECT: The Magical Forest Fairytale
# DESCRIPTION: A dynamic story generator that weaves user inputs into a narrative
#              using F-strings and ends with a user-controlled twist.
# KEY CONCEPTS: F-Strings, String Manipulation (.lower), Conditional Logic.
# -----------------------------------------------------------------------------

print("In the dark of the night, a witch emerged from the edges of the forest and sees a stranger approaching her path.\nShe decides to greet the stranger. Welcome, you are about to enter the gates into the magical forest!\n")

name = input("What is your name?\n")

age = int(input("Are you lost, how old are you?\n"))

print("What are you doing here alone, wandering into the woods at night? You mustn't be alone entering the forest, I will give you a companion for your travels.")

favourite_animal = input("What is your favourite animal?\n").lower()

print("Treat your companion well, you must help each other to make it out to the other side.\nNow I must depart but before I go I will leave you with a powerful weapon to help protect you on your journey.")

magical_item = input("You have a choice from three items, a wand, a shield or a mystical potion.\nUse the wand to cast one spell on your enemy..\nor use the shield to protect you from three powerful attacks..\nor you can drink this potion to make you invincible but only for 5 mins...What have you chosen?\n").lower()

print("A clever choice. Lastly, here is a warning.\nThere are three gates to enter into the magical forest.\nThe gate you enter will determine the monster you must defeat!")

number = int(input("Go ahead and pick a gate number now..\n"))
print()
print("The old witch watched the stranger enter the forest, she pulls out a book and opens it to an empty page.\nVery slowly, words begin to appear. Curious as ever, the old witch reads out what is being written..\n")

story = (
      f"One dark night, {name}, who was {age} years old, was in a hurry to get home and decided to take a shortcut and go through the magical forest.\n"
      f"At the edges of the gates, {name} encountered an old witch who had asked if they were going in alone.\n"
      f"The old witch had offered {name} a companion in the form of {name}'s favourite animal.\n{name} chose a {favourite_animal}. The old witch also gave a choice of one magical item to help fight the monster that lived inside.\n{name} had a choice of three items..a wand, a shield or a potion.\nThe wand to cast one spell, the shield to protect from what hid behind the shadows and a potion to make the drinker invincible but only for 5 mins.\n{name} chose the {magical_item}. "
      f"There were three entrances to the forest and {name} chose gate {number}.\nBut before entering, the old witch gave one final warning, the chosen gate had decided which monster {name} will have to fight to make it out alive.\n"
      f"The old witch watched {name} enter the gates knowing full well the dangers that lived inside darkness.\n"
)

print(story)

twist_1 = (f"But there is a twist to this tale..\nThe person reading this will decide which monster the stranger will face inside the forest. You have a choice of three.\nA two headed fire breathing dragon,\nA giant snake whose venomous bite can kill its prey in an instant,\nor a giant spider that can multiply itself.\n"
         f"What will be the fate of {name}?\n")

print(twist_1)

choice_3 = input("What say you reader, which monster will the stranger face inside the forest? A dragon, a snake or a spider?\n").lower()

if choice_3 == "dragon":
      print("Very well, let us hope they will not be incinerated by the dragon's fire!")

elif choice_3 == "snake":
      print("Very well, let us hope they will not be bitten by the venomous snake!")

elif choice_3 == "spider":
      print("Very well, let us hope they will not be trapped in the spider's web!")
else:
      print("There are no monsters of that name, now you are trapped in the forest forever!")