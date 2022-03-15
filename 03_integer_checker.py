# checks input is a number that is more then zero
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


# Main Routinte goes here

keep_going = ""
while keep_going == "":
    print()
    # ask user for integer (must be more then / equal to 0)
    var_integer = num_check("Enter an integer: ", 0)
    print()

    # ask for height and width of image (must be more than / equal to 1)
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)
