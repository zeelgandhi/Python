films= {
    "Finding dory" :[3,5],
    "Bourne": [18, 6],
    "Padmaavat": [10,0],
    "Tarzan": [12,5]
    }
while True:

    choice=input("Which movie would you want to watch?: ").strip().capitalize()

    if choice in films:
        age = int(input("How old are you?").strip())
        if age>= films[choice][0]:

            num_seats= films[choice][1]

            if num_seats >0 :
                print("Enjoy the movie")
                films[choice][1] = films[choice][1]-1
            else:
                 print("Sorry, we are sold out!")
        else:
            print("you are too young to watch")
    else:
        print("We dont have that movie....")
