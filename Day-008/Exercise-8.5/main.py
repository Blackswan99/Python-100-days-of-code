alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(message,coding,distance):
    processed_message = ""
    for char in message:
        position = alphabet.index(char)
        if coding == "encode":
            position_new = position + distance
            if position_new > 25:
                position_new -= 26
            char_new = alphabet[position_new]
            processed_message += char_new 
        elif coding == "decode":
            position_new = position - distance
            if position_new < 0:
                position_new += 26
            char_new = alphabet[position_new]
            processed_message += char_new 
        else:
            print("Unknown direction.")
            exit()           
    print(processed_message)
