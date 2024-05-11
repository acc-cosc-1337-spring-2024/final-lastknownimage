class Stock:
    def __init__(self, symbol, companyname):
        self.__symbol = symbol
        self.__companyname = companyname
    def get_symbol(self):
        return self.__symbol
    def get_companyname(self):
        return self.__companyname
def main():
    stocks = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    print("Stock report")
    print("---")
    for stock in stocks:
        print(f"Company: {stock.get_companyname()}, Symbol: {stock.get_symbol()}")

if __name__ == "__main__":
    main()