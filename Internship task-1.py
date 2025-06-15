def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if mode == 'e':
    print("Encrypted Message:", caesar_cipher(message, shift))
elif mode == 'd':
    print("Decrypted Message:", caesar_cipher(message, shift, decrypt=True))
else:
    print("Invalid choice. Please enter 'e' or 'd'.")
