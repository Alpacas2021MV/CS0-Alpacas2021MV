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

def compare_lists(list1, list2):
    for i in range(len(list1)):
        if (list1[i] != list2[i]): 
            print(f"There is a mismatch at index {i}: {list1[i]} and {list2[i]}") 
            break

def print_tictactoe_board(board):
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    for i in range(len(board)):
        #print("|", end = '')
        for space in range(len(board[i])):
            print(f"{board[i][space]}", end = '')
            if (space != 2):
                print(" |", end = '')
        print()
        if (i != 2):
            print("-----")

def check_winner(board):
    # Check Horizontal Victory
    for i in range(len(board)):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            print(f"{board[i][0]} wins the game!")

def main():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(f"Initial Board: ")
    print_tictactoe_board(board)
    board[0][1]= 'X'
    print(f"After X moves: ")
    print_tictactoe_board(board)
    board [1][1] = 'O'
    print(f"After O moves: ")
    print_tictactoe_board(board)
    board[2][0] = 'X'
    print(f"After X moves: ")
    print_tictactoe_board(board)
    board[1][2]: 'O'
    print(f"After O moves: ")
    print_tictactoe_board(board)
    board[1][0]: 'X'
    #numlist1 = [42, 15, 23, 84]
    #numlist2 = [42, 15, 23, 83]
    #compare_lists(numlist1, numlist2)
    #for i in range(len(numlist1)):
        #numlist1[i] = numlist1[i]* 10
        #print(numlist1)
    #somenums = [42, 15, [843, ['purple', [82.4, 152.241]], 123], "ab", 5]
    #len_of_list = len(somenums[4])
    #print(somenums)
    #explode_list(somenums)

if __name__ == "__main__":
    main()