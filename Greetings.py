from random import choice as randomChoice

def isGreeting(userInput):
    """Returns Boolean indicating if user input was a greering."""
    greetings = ["hello", "hi"]
    for word in greetings:
        if word in userInput:
            return True
    return False

def respond():
    """Prints a response to user greeting"""
    responses = ["alright", "hiya"]
    out = randomChoice(responses)
    print(out)
