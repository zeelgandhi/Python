import random

class Pound:

#constructor parameter (dont write return inside the construc.)
    def __init__(self,rare=False):

        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
        
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin Spent")
        
    


# coin1.colour="greenish"
# coin1.colour
# 'greenish'
 
# >>> coin1.value = 1.25
# coin1.value
#1.25
# coin2 = Pound()
# coin2.value
# 1.0
