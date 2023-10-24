# Michael Kuzminkisy
def encode(number):
    encoded = []
    for i in number:
        encoded.append(str(int(i)+3))
    return ''.join(encoded)


if __name__ == '__main__':

    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 0:
            break

        elif option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')
