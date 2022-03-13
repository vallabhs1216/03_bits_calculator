# checks input is a number that is more then zero
def num_check (question, low):



    valid = False
    while not valid:

        error = "Please enter a number that is more than "
        "(or equal to) {}".format(low)

        try:
            
            # ask user to enter number
            response = int(input(question))

            # checks number is more than zero
            if response > low:
                return response
            
            # output error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)

