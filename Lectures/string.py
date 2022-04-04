import string
def main():
    str_string = "The next Tuesday is tomorrow"
    lower_string = ""
    for ch in str_string:
        if ch in string.ascii_uppercase:
            ch = ch.lower()
        elif ch in string.whitespace:
            ch = '-'
        lower_string += ch
    print(lower_string)












    #KeepRunning = True
    #counter = 0
    #while(KeepRunning):
    #    print(counter)
    #    counter += 1
    #    runagain = input("Do you want to keep running [Y/N]? ")
    #    if (runagain.lower() == "y" or runagain.lower() == "yes"):
    #        print("Ok let's go again")
    #    else: 
    #        print("Goodbye")
    #        KeepRunning = False


    #str_string = "The next weekend is tomorrow"
    #print(str_string.split())
    #sub_str_loc = str_string.find("weeend")
    #if (sub_str_loc == -1):
    #    print("Substring was not found!")
    #else:
    #    print(str_string[sub_str_loc:sub_str_loc+len("weekend")])

    #print(str_string[-1::-1])
    #print(str_string[::1])

    #counter = -1
    #While loop
    #while (counter >= -len(str_string)):
    #    print(str_string[counter])
    #    counter -= 1

    #For loop
    #for ch in str_string: 
    #    print(ch)

main()