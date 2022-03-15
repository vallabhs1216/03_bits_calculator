# checks user choice is 'interget', 'text' or 'image'
from cgitb import text


def user_choices():

    valid = False
    while not valid:

        response = input("File type (interger / text / image ): ").lower()

        if response == "text" or response == "t":
            return "text"

        else:
            # if response is not balid, output and error
            print("Please choose a valid file type!")
            print()

    
# Main routine goes here
data_type = user_choices()
print("You chose", data_type)

print