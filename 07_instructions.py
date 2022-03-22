# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration, style):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)
    top_bottom = decoration * len(statement)

    if style == 1:

        print()
        print(statement)
        print()

    else:
        print()
        print(top_bottom)
        print(statement)
        print(top_bottom)
        

    return ""


# Displays intrustions / information
def instructions():

    statement_generator("Instructions / Information", "=", 3)
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program asumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 btis per character)." ) 
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# main routine goes here
instructions() 