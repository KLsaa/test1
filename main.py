from Greetings import isGreeting, respond
from Name import askName, giveName

# Loop below runs my very basic chatbot

while True:
    fromUser = input("%%% ")
    if fromUser in ["exit", "quit"]:
        break
    elif isGreeting(fromUser):
        respond()
    else:
        giveName()
        askName()
        
