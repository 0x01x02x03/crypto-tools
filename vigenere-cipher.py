#!/usr/bin/python3

from itertools import cycle
import functools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(key, plaintext):
    pairs = zip(plaintext, cycle(key))
    ciphertext = ''

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) + alphabet.index(y), pair)
        ciphertext += alphabet[total % 26]

    return ciphertext.lower()


def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    plaintext = ''

    for pair in pairs:
        total = functools.reduce(lambda x, y: alphabet.index(x) - alphabet.index(y), pair)
        plaintext += alphabet[total % 26]

    return plaintext



def main():
    print("[*] Welcome to Vigenere Cipher tool")
    print("[*] Would you like to encrypt [E] or [D] decrypt the message?")
    mode = input("[*] Enter your chooice: ").upper()
    if mode == "E":
        plaintext = input("[*] Please enter your message: ")
        key = input("[*] Now enter your key: ")
        encrypted = encrypt(key, plaintext)
        print("[*] Encrypting...")
        print('[*] Encrytped: %s' % encrypted)
    if mode == "D":
        ciphertext = input("[*] Please enter your message: ")
        key = input("[*] Now enter your key: ")
        decrypted = decrypt(key, ciphertext)
        print("[*] Decrypting...")
        print('[*] Decrypted: %s' % decrypted)


if __name__ == '__main__':
    main()
