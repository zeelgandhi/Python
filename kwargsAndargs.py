 #
 def add(*numbers):
	total = 0
	for number in numbers:
		total = total+number
	return(total)

add(1,2,5,6,8) #this will give solution
#
dictionary = {"name":"Milin","age":24,"like":"Pyhton"}
>>> about(**dictionary)
'Meet Milin! They are 24 years old and they like Pyhton.'
>>> dictionary = {"age":24,"name":"Milin","like":"Pyhton"}
>>> about(**dictionary)
'Meet Milin! They are 24 years old and they like Pyhton.'
##
def foo(**kwargs):
	for key, value in kwargs.items():
		print("{}:{}".format(key,value))

		
>>> foo(zeel="female",milin="male")
zeel:female
milin:male


#args-arguments
#kwargs-key word arguments
