letters_to_numbers = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,"u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ".": 27, "?": 28, "'": 29, ",": 30}
numbers_to_letters = {0: " ", 1 : "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t",21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z", 27: ".", 28: "?", 29: "'", 30: ","}
PRECISION_NUMBER = 100

random_digits_realigned = open("random_digits_realigned.txt","w+")
counter = 0

with open('random_digits.txt',"r") as file:
    for i in range(PRECISION_NUMBER):
        for line in file:
            random_digits_realigned.write(line[counter])
        file.seek(0)
        counter += 1

random_digits_realigned.close()

encryptedText = open("encryptText.txt","w+")
plainText = open("plainText.txt", "r")

random_digits_realigned = open("random_digits_realigned.txt","r")
key = random_digits_realigned.readline()
random_digits_realigned.close()


def encrypt_plain_text(dig):
    encryptedText = open("encryptText.txt", "w+")
    plainText = open("plainText.txt", "r")
    counter = 0
    for line in plainText:
        for letter in line:
            if letter == "\n":
                break
            else:
                number = (int(letters_to_numbers[letter.lower()]) + int(dig[counter])) % 31
                counter += 1
                encryptedText.write(numbers_to_letters[number])
        encryptedText.write("\n")
    encryptedText.close()
    plainText.close()

def decrypt_text(dig):
    encryptedText = open("encryptText.txt", "r")
    plainText = open("decryptedText.txt", "w+")
    counter = 0
    for line in encryptedText:
        for letter in line:
            if letter == "\n":
                break
            else:
                number = (int(letters_to_numbers[letter.lower()])- int(dig[counter])) % 31
                counter += 1
                plainText.write(numbers_to_letters[number])
        plainText.write("\n")
    encryptedText.close()
    plainText.close()



#running the encrypt function and the decrypt function
encrypt_plain_text(key)
decrypt_text(key)
