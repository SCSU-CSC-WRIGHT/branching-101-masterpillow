def main():
    total = 0

    for _ in range(5):
        number = input("Enter a number: ")
        total += int(number)

    print("The running total is: " + str(total))


if __name__ == '__main__':
    main()