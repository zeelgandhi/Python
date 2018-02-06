import datetime

class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}!
Thank you for the purchase on {date}.We hope you are excited about using it. Just as a reminder the purchase total was ${total}.Have a great one!
Team CFE
"""
    def add_user(self,name,amount,email=None):
        name = name[0].upper()+name[1:].lower()
        amount= "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email != None:
            detail["email"]= email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details)>0:
            for detail in self.get_details():
                name= detail["name"]
                amount= detail["amount"]
                date= detail["date"]
                message= self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return[]

obj = MessageUser()
obj.add_user("Justin", 123.32, email="hello@teamcfe.com")
obj.add_user("John", 94.23)
obj.add_user("Emilee",323.4)
print(obj.get_details())

print(obj.make_messages())

default_names = {"Justin","John","Emilee","Jim","Ron","Sandra","Whitney"}
default_amounts = [123.32,94.23,323.4,23,322.122323,32.4,99.99]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.We hope you are excited about using it. Just as a 
reminder the purchase total was ${total}.Have a great one!Team CFE
"""

def make_messages(names,amounts):
    messages = []
    if len(names)==len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            
            name = name[0].upper()+name[1:].lower()