def main():
    in_sek = 1.000
    price = 0
    user_input = 0
    while user_input != "-1":
        print("Press 1 for value change in sek (current ",in_sek,") \nPress 2 for adding merchendise \nPress 3 to summerize the purches")
        user_input = input("Eneter number (-1 for exit): ")
        if user_input == "1":
            in_sek = input("Enter exchange rate: ")
            continue
        
        if user_input == "2":
            price = 0
            entery = 0
            while entery < 0:
                price = price + entery
                entery = float(input("Enter price on prouduct (exit with negative number): "))
            continue

        if user_input == "3":
            print("The totatl value in forein currentcy is ",price)
            print("The total amount in sek is ", price*in_sek)
            continue
        if user_input != -1:
            print("The entery number do not countribue to anyting")

if __name__ == "__main__":
    main()

