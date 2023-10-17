alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

playing = "yes"
while playing == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    while direction != "encode" and direction != "decode":
        direction = input(
            "Input a valid direction, 'encode' to encrypt or 'decode' to decrypt\n")
        print(direction)

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 25

    def encrypt_text(plain_text, shift_amount):
        message = ""
        for char in plain_text:
            if char in alphabet:
                new_position = alphabet.index(char) + shift_amount
                if new_position < len(alphabet):
                    message += alphabet[new_position]
                else:
                    message += alphabet[new_position - len(alphabet)]
            else:
                message += char
        print(f"The {direction}d text is: {message}")

    def decrypt_text(plain_text, unshift_amount):
        message = ""
        for char in plain_text:
            if char in alphabet:
                new_position = alphabet.index(char) - unshift_amount
                if new_position >= 0:
                    message += alphabet[new_position]
                else:
                    message += alphabet[new_position + len(alphabet)]
            else:
                message += char
        print(f"The {direction} text is: {message}")

    def user_direction(check_action):
        if check_action == "encode":
            encrypt_text(plain_text=text, shift_amount=shift)
        elif check_action == "decode":
            decrypt_text(plain_text=text, unshift_amount=shift)

    user_direction(check_action=direction)

    playing = input("Would you like to play again? Type yes/no\n")

    while playing != "yes" and playing != "no":
        playing = input("Please type yes or no\n")
