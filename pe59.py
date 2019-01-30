import re
sentence = """
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

sentence = re.sub('[,.\s]+', ' ', sentence)
words = sentence.split(" ")
words = set([word.lower() for word in words if word])

def solution(content, key):
    result = []
    length = len(key)
    for i, value in enumerate(content):
        index = i % length
        result.append(content[i] ^ key[index])
    sentence = ''.join([chr(c) for c in result])
    ws = sentence.split(' ')
    count = 0
    for w in ws:
        if w in words:
            count += 1
        if count >= 10:
            return sum(result)


if __name__ == "__main__":
    with open('pe59.txt') as f:
        content = f.read()
        content = content.strip()
        content = content.split(',')
        content = [int(c) for c in content]

        lower = [c for c in range(ord('a'), ord('z') + 1)]
        for i in lower:
            for j in lower:
                for k in lower:
                    r = solution(content, [i, j, k])
                    if r:
                        print(r)
                        exit()

