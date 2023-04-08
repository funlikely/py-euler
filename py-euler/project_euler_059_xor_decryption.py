"""
    XOR decryption
     
    Problem 59
    
    Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard 
    Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
    
    A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given 
    value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the 
    cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
    
    For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of 
    random bytes. The user would keep the encrypted message and the encryption key in different locations, 
    and without both "halves", it is impossible to decrypt the message.
    
    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
    If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the 
    message. The balance for this method is using a sufficiently long password key for security, but short enough to 
    be memorable.
    
    Your task has been made easy, as the encryption key consists of three lower case characters. Using 
    p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
    and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of 
    the ASCII values in the original text.
"""
from typing import List


def decrypt(data: List[int], key: str) -> List[int]:
    int_key = [ord(key[i]) for i in range(3)]
    decrypt_data = [c ^ int_key[i % 3] for i, c in enumerate(data)]
    return decrypt_data


def get_xor_decryption_information():
    file = open('data/project_euler_069.txt')
    data = file.readline().split(',')
    data = [int(d) for d in data]
    print(data)
    print(len(data))
    d = [[int(c) for i, c in enumerate(data) if i % 3 == t] for t in range(3)]
    print(d[0])
    print(d[1])
    print(d[2])
    histograms = [{c: d[j].count(c) for i, c in enumerate(d[j])} for j in range(3)]
    print(histograms[0])
    print(histograms[1])
    print(histograms[2])

    count = 0
    for a, b, c in [(chr(a + 97), chr(b + 97), chr(c + 97)) for a in range(26) for b in range(26) for c in range(26)]:
        key = a + b + c
        decrypt_data = decrypt(data, key)
        decrypt_str = ''.join([chr(c) for c in decrypt_data])

        # using a fold to find the number of decrypted characters that are in the range of A-Z, a-z, 0-9, and spaces
        def f(acc, x):
            return acc + 1 if 97 <= x <= 122 or 65 <= x <= 90 or x == 32 or 48 <= x <= 57 else acc

        accumulator = 0
        [accumulator := f(accumulator, x) for x in decrypt_data]

        if accumulator > 1300:
            print(f"counter = {count}, key = {key}, decrypted characters = {decrypt_str}")
            break
        count += 1

    # used the output to determine that the key is 'exp'.
    # this problem requires some inspection

    return sum([ord(i) for i in decrypt_str])


def main():
    answer = get_xor_decryption_information()
    print(f"The Answer to Project Euler 059 is {answer}")

    # The Answer to Project Euler 059 is 129604


if __name__ == "__main__":
    main()
