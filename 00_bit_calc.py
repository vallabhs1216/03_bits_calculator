# Funtion goes here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# checks user choice is 'integer', 'text' or 'image'
def user_choice():

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
            want_interget = input("Press <enter> for integer or any key for an image ")
            if want_interget == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("Sorry, please choose integer, text or image")
            print()


# checks input is a number more than give value
def num_check (question, low):
    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to) {}".format(low)

        try:
            
            # ask user to enter number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response
            
            # output error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask a user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""


# finds # of bits for 24 bit coloour
def image_bits():

    # get width and height...
    image_width = num_check("Image width: ", 1)
    image_height = num_check("Image height: ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working 
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()


    return ""


# converts decimal to binary and states how 
# many bits are needed to represent the original interger
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # source for code is below
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b}".format(var_integer)


    #cakcukate # of bits (length of string above)
    num_bits = len(var_binary)

     # output answer with working 
    print()
    print("{} is binary is {}".format(var_integer, var_integer))
    print("# of binary is {}".format(num_bits))
    print()

    return ""


# Main Routine goes here


# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")


# Display instructions if user has not used the program before



# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    if data_type == "integer":
        int_bits()

    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()