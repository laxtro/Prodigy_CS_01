def encrypt(t, s):

    r = ""
    for i in range(len(t)):
        char = t[i]
        if char.isupper():
            r += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            r += chr((ord(char) + s - 97) % 26 + 97)
        else:
            r += char
    return r


def decrypt(t, s):

    return encrypt(t, -s)


def main():

    while True:

        print("\n Encryption and Decryption using Caesar Cipher Algorithm")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            t = input("Enter the message to encrypt: ")
            s = int(input("Enter the shift value: "))
            print(f"Encrypted message: {encrypt(t, s)}")

        elif choice == '2':
            t = input("Enter the message to decrypt: ")
            s = int(input("Enter the shift value: "))
            print(f"Decrypted message: {decrypt(t, s)}")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
