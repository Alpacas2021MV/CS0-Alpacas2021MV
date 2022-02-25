'''
Name: Marcos Villarreal
Date: 02/23/21

This program will take in the number of seconds
and convert that to HH:MM:SS

#Step 1: input number of seconds
#Step 2: convert seconds to minutes and hours 
#Step 2a: convert seconds to hours
#Step 2b: convert remianing seconds to minutes
#Step 3: print out HH:MM::SS from inputed seconds
'''
#Step 2

def convert_seconds_time(seconds):
    hours = seconds //3600
    rem_seconds = seconds - (hours * 3600)
    minutes = rem_seconds//60
    rem_seconds = rem_seconds%60
    return hours, minutes, rem_seconds

def tests(): 
    assert convert_seconds_time(3661) == (1, 1, 1)
    assert convert_seconds_time (5280) == (1, 28, 0)
    print(f"All test cases passed")

def main(): 
    tests()
    #Step 1
    seconds = int(input("Please enter the number of seconds: "))

    #Step 2
    hours, minutes, rem_seconds = convert_seconds_time(seconds)

    #3661 seconds = 01:01:01 / 1:1:1
    print(f"The time format of {seconds} seconds is: {hours}:{minutes}:{seconds%60}")

main()