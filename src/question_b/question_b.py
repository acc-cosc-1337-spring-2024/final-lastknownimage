class Stock:
    def __init__(self, symbol, companyname):
        self.__symbol = symbol
        self.__companyname = companyname
    def get_symbol(self):
        return self.__symbol
    def get_companyname(self):
        return self.__companyname

def stock_buyhistory():
    stock_list = {
        "AAPL": Stock("AAPL", "Apple Inc"),
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft")
    }

    print("Stock Buy History:")
    print("---")
    for symbol, stock in stock_list.items():
        print(f"Symbol: {stock.get_symbol()}, Company Name: {stock.get_companyname()}")
def main():
    while True:
        print("\nMenu:")
        print("1) Display stock buy history")
        print("2) Quit")
        option = input("Option: ")
        if option == "1":
            stock_buyhistory()
        elif option == "2":
            print("Shutting down.")
            break
        else:
            print("Stop that. 1 or 2.")

if __name__ == "__main__":
    main()