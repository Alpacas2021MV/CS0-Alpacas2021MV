import sys

def tests():
    pass

def main():
    blimps = []
    for i in range(5):
        blimps.append(input())
    # or blimps = [input() for i in range(5)]. They are the same (creates a list)
    blimp_str = ""
    for i in range(len(blimps)):
        if "FBI" in blimps[i]:
            blimp_str = blimp_str + str(i + 1) + " "
    if blimp_str == "":
        print("HE GOT AWAY")
    else:
        print(blimp_str.strip())

if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "test"):
        tests()
    else:
        main()