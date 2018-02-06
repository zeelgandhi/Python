from py_day_test import  some_rando, make_messages

from py_day_module.make_messages import MessageUser

obj = MessageUser()
obj.add_user("Justin", 123.32, email="hello@teamcfe.com")
obj.add_user("John", 94.23)
obj.add_user("Emilee",323.4)
obj.get_details()

#print(obj.make_messages())

#print(some_rando())

default_names = {"Justin","John","Emilee","Jim","Ron","Sandra","Whitney"}
default_amounts = [123.32,94.23,323.4,23,322.122323,32.4,99.99]


make_messages(default_names,default_amounts)