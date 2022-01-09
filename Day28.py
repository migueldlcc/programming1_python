
def main():
    print("{:20}|{:>10}".format("Transaction Name", "Amount"))
    print("{:-<20}|{:-<10}".format("",""))

    transactions = []

    item = {}
    item['name'] = "Internet fee"
    item['amount'] = 1012

    transactions.append(item)

    item2 = {}
    item2['name'] = "Dogfood"
    item2['amount'] = 1594

    transactions.append(item2)

    for item in transactions:
        print("{:20}|${:8.2f}".format(item['name'], item['amount']/100))


if __name__ == "__main__":
    main()
