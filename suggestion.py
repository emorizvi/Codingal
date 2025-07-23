import re, random

from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)

init(autoreset=True)

# Destination & joke data

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

]

# Helper function to normalize user input (remove extra spaces, make lowercase)

def normalize_input(text):

    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    preference = input("Would you like to go to beaches, mountains or cities")
    preference = normalize_input(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print("How about", suggestion, "? (yes/no)")
        answer = input()

        if answer == "yes":
            print(f"Awesome, enjoy {suggestion}")
        elif answer == "no":
            print("Let's try another place then.")
            recommend()
        else:
            print("I will try again.")
            recommend()
    else:
        print("Sorry, I dont have that type of destination")

def packing_tips():
    place = input("Where are you travelling?")
    days = input("And for how many days?")

    print(f"Tips for going to {place} for {days} days: ")
    print("Pack versatile clothes")
    print("Bring chargers/adaptors")
    print("Check the weather forecast")

def tell_a_joke():
    print(random.choice(jokes))

def chat():
    print("Hello, I'm TravelBot")
    name = input("Your name? ")
    print(f"Nice to meet you, {name}")

    while True:
        user_input = (f"{name}: would you like a suggested destination, packing tips, or a joke?")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_a_joke()
        else:
            print("Please could you rephrase?")

if __name__ == "__main__":
    chat()
    