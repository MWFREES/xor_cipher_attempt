#xor cipher 

key = "markf"
plain_text = "hello"
def xorCipher(plain_text, key):
    cipher_text = ""
    for i in range(len(key)):
        cipher_text += ''.join(chr(ord(plain_text[i])^ord(key[i])))
    
    return cipher_text
test = xorCipher(plain_text,key)
print(test)


