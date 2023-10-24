# Michael Kuzminkisy
def encode(number):
    encoded = []
    for i in number:
        encoded.append(str((int(i) + 3) % 10)) # (RenyPiao) Fix the function to make sure the accurate results
    return ''.join(encoded)


# Renyu Piao
def decode(number):
    decoded = []
    for i in number:
        decoded.append(str((int(i) - 3) % 10))
    return ''.join(decoded)


if __name__ == '__main__':

    encoded_password = None
    orig_password = None

    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 0:
            break

        elif option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')

        elif option == 2:
            orig_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {orig_password}.')
