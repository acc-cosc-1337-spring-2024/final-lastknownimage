def main():
    numbers = []
    for i in range(5):
        number = float(input("Enter a number {}: ".format(i+1)))
        numbers.append(number)
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print("lowest number:", lowest)
    print("highest number:", highest)
    print("sum:", total)
    print("average:", average)

if __name__ == "__main__":
    main()