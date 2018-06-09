lettDict ={'a':1,
           'b':2,
           'c':3,
           'd':4,
           'e':5,
           'f':6,
           'g':7,
           'h':8,
           'i':9,
           'j':10,
           'k':11,
           'l':12,
           'm':13,
           'n':14,
           'o':15,
           'p':16,
           'q':17,
           'r':18,
           's':19,
           't':20,
           'u':21,
           'v':22,
           'w':23,
           'x':24,
           'y':25,
           'z':26,
    }

numDict = {
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e',
    6:'f',
    7:'g',
    8:'h',
    9:'i',
    10:'j',
    11:'k',
    12:'l',
    13:'m',
    14:'n',
    15:'o',
    16:'p',
    17:'q',
    18:'r',
    19:'s',
    20:'t',
    21:'u',
    22:'v',
    23:'w',
    24:'x',
    25:'y',
    26:'z'
    }
    

myKey = ''
phrase = ''
with open('') as waterSource:
    mysterium = waterSource.read()
    


def encrypt(plaintext, key):
    ciphertext = ''
    key_length = len(key)
    n = 0
    for i in range(len(plaintext)):
        if plaintext[i] in lettDict:
            keyness = key[(i-n)%key_length]
            keyVal = lettDict[keyness]
            textVal = lettDict[plaintext[i]]
            codeNum = (keyVal + textVal)%26
            if codeNum == 0:
                codeNum = 26
            ciphertext += numDict[codeNum]
        else:
            ciphertext += plaintext[i]
            n+=1
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    key_length = len(key)
    n = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] in lettDict:
            textVal = lettDict[ciphertext[i]]
            keyness = key[(i-n)%key_length]
            keyVal = lettDict[keyness]
            codeNum = (textVal - keyVal)
            if codeNum <= 0:
               codeNum += 26
            plaintext += numDict[codeNum]
        else:
            plaintext += ciphertext[i]
            n+=1
    return plaintext


coded = encrypt(mysterium,myKey)
decoded = decrypt(coded, myKey)
print(myKey, coded, decoded)


    

        

























##def main():
##    with open('mysterium') as waterSource:
##        plaintext = waterSource.read()
##    print(plaintext)
##
##
##if __name__ == '__main__':
##    main()
