alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        position = alphabet.index(char)
        position_new = position + shift
        if position_new > 25:
            position_new -= 26
        char_new = alphabet[position_new]
        encrypted_message += char_new
    print(encrypted_message)

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        position = alphabet.index(char)
        position_new = position - shift
        if position_new < 0:
            position_new += 26
        char_new = alphabet[position_new]
        decrypted_message += char_new
    print(decrypted_message)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong input.")
