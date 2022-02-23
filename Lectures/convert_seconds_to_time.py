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
#Step 2a
def convert_seconds_to_hours(seconds): 
    hours = seconds // 3600
    return hours

#Step 2b
def convert_seconds_to_minutes(seconds): 
    #print(f"DEBUG: seconds = {seconds}")
    minutes = seconds // 60
    return minutes

def main(): 
    #Step 1
    seconds = int(input("Please enter the number of seconds: "))

    #Step 2
    hours = convert_seconds_to_hours(seconds)
    minutes = convert_seconds_to_minutes(seconds - (hours * 3600))

    #3661 seconds = 01:01:01 / 1:1:1
    print(f"The time format of {seconds} seconds is: {hours}:{minutes}:{seconds%60}")
    pass

main()