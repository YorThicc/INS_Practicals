import time

if __name__ == "__main__":
    
    key = ("QWERTYUIOPLKJHGFDSAZXCVBNM")
    print("Enter the plain-text:")
    while True :
        plain_text = input().strip()
        plain_text = plain_text.replace(" ", "")
        if plain_text.isalpha() :
            break
        else :
            print("Follow the rules. Plain-text should contain only alphabets")
            print("Enter the plain-text :")
            
    for j in range(10) :
        cipher_text = []
        for i in plain_text.upper() :
            cipher_text.append(key[ord(i) - ord('A')])
            
    print("Cipher-text is :")
    print("".join(cipher_text))

