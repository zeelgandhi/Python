for number in range(1,21):
    print(number)
#

for letter in "abcdef":
    print(letter)
    
#

vowels = 0
consonants = 0

for letter in "abcdefghijklmnopquireotxyz":
    if letter.lower() in "aeiou":
        vowels = vowels +1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels" .format(vowels))
print("There are {} consonants" .format(consonants))

#

students = {
    "male": ["Tom", "Charlie", "Milin"],
    "female": ["Zeel", "Sarah", "Emily"]

    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

#

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)
