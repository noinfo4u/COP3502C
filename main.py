# jack smith
def show_menu():
    print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n'
          '\n')
    # turn entry into int and return it
    user_entry = int(input('Please enter an option: '))
    return user_entry

def encode(password):
    # this encodes the password by adding 3 to each digit

    # initialize new encoded password
    encoded_password = ''
    # password is a string
    for character in password:
        digit = int(character) + 3
        if digit >= 10:
            digit = str(digit)[-1]
        encoded_password += str(digit)
    return encoded_password
def main():
    # make a while loop to keep showing the menu
    while True:
        selection = show_menu()
        if selection == 1:
            entry = input('Please enter your password to encode: ')
            encoded_password = encode(entry)
            print('Your password has been encoded and stored!')
        if selection == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {entry}.\n')
        if selection == 3:
            exit()
if __name__ == '__main__':
    main()
