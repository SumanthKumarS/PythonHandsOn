import _init_
import greet
def display(name,module):
    print(name)
    print("Documentation string: ",module)
    

name = input("Enter the senior's name: \n")
name_new = _init_.newname(name)
module = greet.greet_farewell("Hello")
display(name_new,module)
 
