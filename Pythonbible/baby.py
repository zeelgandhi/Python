from random import choice

questions = ["What is your name?" , "Where do u live?", "Why is the sky blue?"]
question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh..okay")
