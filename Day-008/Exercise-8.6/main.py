logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message,coding,distance):
    if distance == 26:
        print("A distance of 26 leeds to message and cipher to be the same.")
        exit()
    if distance > 26:
        distance = distance % 26
    processed_message = ""
    for char in message:
        # check for  numbers
        if char.isdigit() == False:
            # check for symbols
            if char.isalpha() == True:
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
            else:
                processed_message += char    
        else:
            processed_message += char        
    print(processed_message)

run_again="yes"
print(logo)

while run_again.lower() == "yes":
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(message=text,coding=direction,distance=shift)
    run_again = input("Do you want another run (yes/no)? ")
print("Goodbye.")
