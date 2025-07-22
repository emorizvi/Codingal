print("Hello, I am your friendly AI chatbot")

name = input("What is your name? ")

print(f"Hello, {name} how are you (good/bad)")

mood = input().lower()

if mood == "good":
    print("It's nice to hear that!")
elif mood == "bad":
    print("Sorry to hear that, hope you feel better soon")
else:
    print("Sometimes it is hard to put feeling into words")

print(f"Anyways, it was nice getting to know you, {name}")
print("Goodbye!")