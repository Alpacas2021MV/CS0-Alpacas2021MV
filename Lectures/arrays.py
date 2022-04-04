def explode_list(list_element):
    for i in list_element:
        #if str(type(i)) == "<class 'list'>":
        if isinstance(i, list):
            explode_list(i)
            #for j in i:
            #    if isinstance(j, list) or isinstance(j, str):
            #        for k in j:
            #            if isinstance(k, list) or isinstance(k, str):
            #                for l in k:
            #                    print(l)
        else: 
            if isinstance(i, str):
                for j in i:
                    print(j)
            else:
                print(i)
        #print(i)

def main():
    somenums = [42, 15, [843, ['purple', [82.4, 152.241]], 123], "ab", 5]
    #len_of_list = len(somenums[4])
    #print(somenums)
    explode_list(somenums)

if __name__ == "__main__":
    main()