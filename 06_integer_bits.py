# checks input is a number more than a given value
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


#  converts decimal to binary and states how many bits are needed to represent the original interger
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
    print("# of bits is {}".format(num_bits))

    return ""

# Main routine

int_bits