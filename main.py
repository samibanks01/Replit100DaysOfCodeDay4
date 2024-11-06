print("""Welcome to your adventure simulator. 
  I am going to ask you a bunch of questions and
  then create an epic story with you as the star!""")

name = input("What is your name?")
enemy = input("What is your worst enemy’s name?")
superpower = input("What is your superpower?")
house = input("Where do you live?")
food = input("What is your favorite food?")

print("Hello", "\033[32m", name,"!","\033[0m" "Your ability to", "\033[33m", superpower, "\033[0m", "will make sure you never have to look at", enemy, "again. Go eat", food, "as you walk down the streets of", house, "and use", "\033[33m", superpower, "\033[0m", "for good and not evil!")
