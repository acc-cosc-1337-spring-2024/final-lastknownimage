def make_mult_table():
    table = []
    for i in range(1,11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table
def display_mult_table(table):
    print("Multiplication table:")
    for row in table:
        for num in row:
            print(f"{num:4}", end="")
        print()
def main():
    while True:
        mult_table = make_mult_table()
        display_mult_table(mult_table)
        choice = input("Go on? (y/n): ")
        if choice.lower() != "y":
            print("Quitting.")
            break

if __name__ == "__main__":
    main()