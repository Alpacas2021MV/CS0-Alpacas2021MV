from sys import *

def main():
    my_dictionary = {}
    #my_dictionary2 = dict()
    my_key = "apple"

    my_dictionary[my_key] = 42
    my_dictionary["Apple"] = 24
    my_dictionary[0] = "purple"
    my_dictionary['red'] = [42, 24, 15, 5, "rain"]
    my_dictionary["second_dictionary"] = {1:"apple", "computer": "mouse", "green": [42, 24, 15]}

    my_dictionary["red"].append(42)

    print(f"{my_dictionary.values()}")

    print(f"{my_dictionary.keys()}")
    #for k in my_dictionary.keys():
    #    print(f"{my_dictionary[k]}")

    #print(my_dictionary)
    #for k, v in my_dictionary.items():
    #    print(f"{k}: {v}")



    #print(type(my_dictionary["red"]))

    #if my_dictionary.get("apple") != None:
    #    my_key = "Bob"
    #    my_dictionary[my_key] = "Pear"
    
    #print(f"{my_dictionary}")
    #print(f'{my_dictionary["second_dictionary"]["green"][1]}')
    #print(f'The value in the dictionary key apple is: {my_dictionary["apple"]}')
    #print(f'The value in the dictionary key apple is: {my_dictionary[0]}')
    #print(f'The value in the dictionary key red is: {my_dictionary["red"]}')
    #my_list = []
    #my_list2 = list()

if __name__ == "__main__":
    if (len(argv) == 2 and argv [1] == "test"):
        test()
    else:
        main()