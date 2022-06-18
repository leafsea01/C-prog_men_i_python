


def main():
    in_sek = "1.000"
    price = 0
    user_input = "0"
    while user_input[0] != "-1":
        print("\nPress 1 for value change the value in sek (current value is",float(in_sek[0]),"in sek) \nPress 2 for adding merchendise \nPress 3 to summerize the purches")
        user_input = input("Eneter number (-1 for exit): ").split()
        if user_input[0] == "1":
            in_sek = input("Enter exchange rate: ").split()
            continue
        
        if user_input[0] == "2":
            price = 0
            entery = 0
            while entery >= 0:
                price = price + entery
                entery = float(input("Enter price on prouduct (exit with negative number): "))

            print("The totatl value in forein currentcy is ",price,end="")
            continue

        if user_input[0] == "3":
            print("The totatl value in forein currentcy is ",price)
            print("The total amount in sek is ", price*float(in_sek[0]))
            continue
        if user_input[0] != "-1":
            print("The entery number do not countribue to anyting")

if __name__ == "__main__":
    main()

