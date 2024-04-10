def encode(password):
    new = ''
    for item in password:
        item = int(item)
        item += 3
        if item >= 10:
            item -= 10
        new += str(item)
    return new


def decode(password):
    new =''
    for item in password:
        item = int(item)
        item -= 3
        if item < 0:
            item += 10
        new += str(item)

    return new


def main():

    encoded = []

    while True:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")


        elif choice == 2:
            decoded = decode(encoded)
            new_pass = ""
            for item in decoded:
                new_pass += str(item)


            print(f"The encoded password is {encoded}, and the original password is {decoded}")

        elif choice == 3:
            break











if __name__ =="__main__":
       main()