def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = input("Enter the word: ")
s = input("Enter a key except 3: ")
s = int(s)
if s == 3:
    print("Invalid Key")
else:
    print ("Text  : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + encrypt(text,s))
