
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


# finds # of bits for 24 bit coloour
def image_bits():

    # get width and height...
    image_width = num_check("Image width")
    image_height = num_check("Image height")

    # calculate # of pixels
    num_pixels = image_width * 24

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working 
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()


    return ""


# Main routine goes here
image_bits()