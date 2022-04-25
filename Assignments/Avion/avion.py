'''
Name: Marcos Villarreal
Date: 04/06/22

This program will solve the Kattis problem titled "Avion" which would point out all CIA blimps 
'''

def cia_blimps(): 
    num = []
    for i in range(5): 
        blimps = input()
        if ('FBI' in blimps):
            num.append(i+1)

    else: 
        print("HE GOT AWAY!")
         

def main(): 
    cia_blimps()

if __name__ == "__main__":
    main()