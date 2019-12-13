import time
import random

# z is ord value 122 and a is 97

# This function encrypts a sentence with a given key. Used to encrypt sentence from sentences.txt for the program to use.


def encrypt_sentence(sentence, key):
    temp = ""
    for character in sentence:
        if (ord(character) > 122 or ord(character) < 97):
            temp = temp + character
        elif (ord(character) + key > 122):
            temp = temp + chr(96 + (ord(character) + key - 122))
        else:
            temp = temp + chr(ord(character) + key)
    return temp

# This function goes through the proces of determining what the key is for the encrypted sentence.


def decrypt(sentence):
    split = sentence.split(" ")
    i = 1
    # Shift through the sentence for all key possibilities --- # of chars in alphebet == 26
    prev_key = 0
    while i <= 26:
        val = 0
        for word in split:
            keyed = ""
            for char in word:
                if (ord(char) > 122 or ord(char) < 97):
                    pass
                elif (ord(char) - i < 97):
                    keyed = keyed + chr(122 - (96 - ord(char) + i))
                else:
                    keyed = keyed + chr(ord(char) - i)
            if ((len(keyed) == 1) and (keyed != 'a' or keyed != 'i')):
                continue
            for word in words:
                if keyed == word:
                    if len(keyed) > 3:
                        return decrypt_sentence(sentence, i)
                    else:
                        prev_key = i
        i += 1
    if (prev_key != 0):
        return decrypt_sentence(sentence, prev_key)
    return "COULD NOT DETERMINE KEY"

# This fucntion goes through the process of decrypting a caesar cipher sentence of a certain key


def decrypt_sentence(sentence, key):
    start_time = time.time()
    temp = ""
    for char in sentence:
        if (ord(char) > 122 or ord(char) < 97):
            temp = temp + char
        elif (ord(char) - key < 97):
            temp = temp + chr(122 - (96 - ord(char) + key))
        else:
            temp = temp + chr(ord(char) - key)
    print(temp)
    return key


words = open("words.txt", "r").read().lower().split("\n")
sentences = open("sentences.txt", "r").read().split(
    "\n")  # <- Uncomment for sentences testing
# sentences = open("quotes.txt", "r").read().split("\n")  # <- Uncomment for quotes testing


# encrypt all of the sentences of random key
i = 0
correct = 0
for sentence in sentences:
    key = random.randint(1, 26)  # Does not handle > 26 or 0
    sentenceE = encrypt_sentence(sentence.lower(), key)
    sentenceD = decrypt(sentenceE)
    print(str(i+1) + ": Encrypted key: " + str(key) +
          " --- Returned Key: " + str(sentenceD) + "\n")
    if (sentenceD == key):
        correct += 1
    i += 1
print("Total: " + str(i) + " --- Correct: " + str(correct))
print("Accuracy Ratio: " + str(correct/i))
