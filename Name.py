from random import choice as randomChoice

def giveName():
    """Chooses a random name for chatbot"""
    names = ["chatbot3000", "bob"]
    out = randomChoice(names)
    print("My name is " + out)

def askName():
    """Asks user their name and greets"""
    userName = input("What is your name? ")
    print("Nice to meet you " + userName)
