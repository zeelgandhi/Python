class Human():
    height = 5.5
    colour = "White"
    place = "India"
    num_eyes = 2
    def can_walk(self):
        return "Yes"
    def speak_language(self):
        return "english"

class Milin(Human):
    name = "bhavsar"
    place = "USA"
    def speak_language(self):
        return "gujarati"

class Zeel(Human):
    name = "gandhi"

Zeel_obj = Zeel()
Milin_obj = Milin()
print(Milin_obj.speak_language())
Milin_obj.name = input("What is your name for Milin_obj?: ").lower().strip()
Zeel_obj.name = input("What is your name for Zeel_obj?: ").lower().strip()
if  Zeel_obj.name != "gandhi":
    print("Name not recognized")

elif Milin_obj.name != "bhavsar":
        print("Name not recognized")

else:
    print("welcome")


    
    
