from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += alphabet[(index + shift_amount) % 26]
        else:
            encrypted_text += char
    print(encrypted_text)

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            decoded_text += alphabet[(index - shift_amount) % 26]
        else:
            decoded_text += char
    print(decoded_text)


def caesar(choice, text, shift):
    if choice == "encode":
        encrypt(text, shift)
    elif choice == "decode":
        decrypt(text, shift)
    else:
        print("Only encode or decode")


print(logo)
con = "yes"
while con.lower() == "yes":
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(choice, text, shift)
    con = input("Yes to go again, No to stop: \n")
