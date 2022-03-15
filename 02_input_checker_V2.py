# checks user choice is 'interget', 'text' or 'image'
def user_choices():

    # List of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic","p"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image ): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integet = input("Press <enter> for integer or any key for an image ")
            if want_integet == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("Sorry, please choose integer, text or image")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choices()
    print("You chose", data_type)

    print()