def decoder(encrypted_password):
    # this decodes the password by subtracting 3 from each digit

    # initialize new decoded password
    decoded_password = ''
    # password is a string
    for character in encrypted_password:
        digit = int(character) - 3
        if digit <= -1:
            digit += 10
        decoded_password += str(digit)
    return decoded_password
