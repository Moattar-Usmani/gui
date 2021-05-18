def farenheit():
    f = int(input("Enter Temperature in Farenheit"))
    faren = 5 *(f - 32) / 9
    print(faren)


def celsius():
    c = int(input("Enter Temperature in Celsius"))
    cel = (9 / 5) * c + 32
    print(cel)


def temperature():
    print ("1. Temperature in Farenheit")
    print ("2. Temperature in Celsius")
    while True:
        choice = input("enter a choice to see conversion")
        if choice in ('1' , '2'):
            if choice == '1':

              farenheit()

            elif choice == '2':

                celsius()
temperature()