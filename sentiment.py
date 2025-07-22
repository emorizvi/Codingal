import colorama
from colorama import Style,Fore
from textblob import TextBlob

colorama.init()
print("Welcome to the sentiment spy")
name = input("What's your name? ")

if not name:
    name = "Mystery"

conversation_history = []

print(f"/n{Fore.CYAN}Hello Agent {name}")
print("Please enter your sentiment to analyze")
print(f"Type 'reset', 'history', or 'exit'")

while True:
    user_input = input()
  
    print(f"Type 'reset', 'history', or 'exit'")

    if not user_input:
        print("Please enter a valid command")
    
    elif user_input.lower() == "exit":
        print("Goodbye")
        break

    elif user_input == "reset":
        print("Coversation history has been cleared")
        conversation_history.clear()
        continue

    elif user_input == "history":
        if not conversation_history:
            print("No history to show")
        else:
            print("Coversation history:")
           #for idx,(text, polarity, setniment_type) in emurate(conversation_history, start = 1):
            if setniment_type == "positive":
                    emoji = "😊"
            elif setniment_type == "negative":
                    emoji = "☹️"
            else:
                    emoji = "😐"
        continue
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        setniment_type = "postive"
    elif polarity < -0.25:
        setniment_type = "negative"
    else:
        setniment_type = "neutral"
    print(f"The sentiment type is {setniment_type}")
    conversation_history.append((user_input, polarity, setniment_type)