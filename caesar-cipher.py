#!/usr/bin/python
import sys

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, shift):

    result = ''

    for letter in plaintext.lower():
        try:
            i = (key.index(letter) + shift) % 26
            result += key[i]
        except ValueError:
            result += letter

    return result.lower()

def decrypt(shift, ciphertext):
    result = ''

    for letter in ciphertext:
        try:
            i = (key.index(letter) - shift) % 26
            result += key[i]
        except ValueError:
            result += letter

    return result

def brute(ciphertext):
    alphabet = list(key)
    plaintext = ""
    shift = 1

    while shift <= 26:
     for letter in ciphertext:
      if letter in alphabet:
       plaintext += alphabet[(alphabet.index(letter)+shift)%(len(alphabet))]
     print("Shift: " + str(shift))
     print("Ciphertext: " + ciphertext)
     print("Plaintext: " + plaintext)
     shift = shift + 1
     plaintext = ""


def main():
    print("Would you like to encode [E], decode [D] or brute force [B]? ")
    mode = input("Enter your chooice: ")
    if mode == 'E':
        plaintext = input('Please enter your message: ')
        shift = int(input('Enter the shift: '))
        encrypted = encrypt(plaintext, shift)
        print('[*] Shift: %s' % shift)
        print('[*] Plaintext: %s' % plaintext)
        print('[*] Ciphertext: %s' % encrypted)
    elif mode == 'D':
        ciphertext = input('Please enter your message: ')
        shift = int(input('Enter the shift: '))
        decrypted = decrypt(shift, ciphertext)
        print('[*] Shift: %s' % shift)
        print('[*] Encrypted: %s' % ciphertext)
        print('[*] Decrypted: %s' % decrypted)
    elif mode == 'B':
        ciphertext = input('Please enter your message: ').lower()
        brute(ciphertext)
    else:
        print('Error')
        sys.exit()

if __name__ == '__main__':
    main()
