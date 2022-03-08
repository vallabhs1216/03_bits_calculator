# checks user choice is 'interget', 'text' or 'image'
def user_choices():

    # List of valid responses
    text_ok = ["text", "t", "txt"]
    interger_ok = ["interger", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (interger / text / image ): ").lower()

        # Checks for valid response and returns text, interger or image

        if response in text_ok:
            return "text"

        elif response in interger_ok:
            return "interger"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_interget = input("Press <enter> for interger or any key for an image ")
            if want_interget == "":
                return "interger"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()
        
# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choices()
    print("You chose", data_type)

    print()