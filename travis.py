known_users=["Zeel" , "Milin", "Gandhi"]

while True:
    print("Welcome to WF")
    name=input("What is your name?: ").strip() .capitalize()   

    if name in known_users:
        print("Hello {}".format(name))
        remove= input("Would you like to be removed from the system(y/n)?: ").strip().lower()

        if remove== "y":
            known_users.remove(name)
        elif remove=="n":
                print("no problem!")
         
    else:
        print("Hmmm i dont i have met you yet {}".format(name))
        add_me=input("Would u like to b added to the systemm(y/n)?: ").strip().lower()
        if add_me=="y":
            known_users.append(name)
        elif add_me=="n":
                print("No worries!")
          
