#data
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
print(logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


#decode script
def caesar(original_text, original_shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        original_shift *= -1
    for n in original_text:
        if n in alphabets:
            shifted_index = alphabets.index(n) + original_shift
            shifted_index %= len(alphabets)
            output_text += alphabets[shifted_index]
        elif n in numbers:
            shifted_index = numbers.index(n) + original_shift
            shifted_index %= len(numbers)
            output_text += numbers[shifted_index]
        else:
            output_text += n
    return output_text
# user inputs and output for cipher

condition_for_loop = True
while condition_for_loop:
    ask_user = input("Would you like to encode or decode?: \n").lower()
    if ask_user == "encode":
         input_message = input("What is your message?:\n").lower()
         shift_key = int(input("What is the shift value?:\n"))
         encoded_word = caesar(original_text=input_message, original_shift=shift_key, encode_or_decode=ask_user)
         print(f"The encrypted word is:\n{encoded_word}")
         condition_for_loop = False
    elif ask_user == "decode":
         input_message = input("What is your message?:\n").lower()
         shift_key = int(input("What is the shift value?:\n"))
         decoded_word = caesar(original_text=input_message, original_shift=shift_key, encode_or_decode=ask_user)
         print(f"The decrypted word is:\n{decoded_word}")
         condition_for_loop = False
    elif ask_user == "exit":
         print("Exiting program")
         condition_for_loop = False
    else:
        print("Please select from Encode or decode. For exit - type 'exit'")
        condition_for_loop = True