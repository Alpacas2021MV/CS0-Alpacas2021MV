def main():
    num = int(input())
    lines = [input() for _ in range(num)]

    print(f"{lines}")
    for line in lines:
        simon(line)