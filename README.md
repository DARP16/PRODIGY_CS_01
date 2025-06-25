# 🔐 Caesar Cipher – Internship Task

A simple command-line tool to encrypt and decrypt messages using the classic Caesar Cipher technique. Built as part of a cybersecurity internship task to demonstrate basic cryptographic principles using Python.

---

## 📖 About

The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. This Python program allows the user to input a message, choose a shift value, and select whether to encrypt or decrypt the message.

---

## ✨ Features

- Supports both encryption and decryption
- Works with both uppercase and lowercase letters
- Preserves non-alphabetic characters (e.g., spaces, punctuation)
- Simple, readable, and efficient Python logic

---

## 🛠 Tech Stack

| Technology | Role                   |
|------------|------------------------|
| Python     | Core scripting language |
| CLI        | User interaction        |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. You can check by running:

python --version

### Installation

1. Clone the repository or download the file:


2. Run the script:
python Internship\ task-1.py


---

## 🧪 Usage

Follow the prompts in your terminal:

Enter your message: Hello World!
Enter shift value: 3
Type 'e' to encrypt or 'd' to decrypt: e
Encrypted Message: Khoor Zruog!

To decrypt:
Enter your message: Khoor Zruog!
Enter shift value: 3
Type 'e' to encrypt or 'd' to decrypt: d
Decrypted Message: Hello World!


---

## 🔎 Core Logic

The program uses this logic to shift characters:

if char.isalpha():
base = ord('A') if char.isupper() else ord('a')
result += chr((ord(char) - base + shift) % 26 + base)

## 📄 License

This project is open-source and available under the MIT License.


