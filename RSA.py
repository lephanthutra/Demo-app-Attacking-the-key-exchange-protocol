import rsa
 
def generate_keys():
   publicKey, privateKey = rsa.newkeys(512) 
   return publicKey, privateKey

def encrypt(message, publicKey):
    encMessage = rsa.encrypt(message.encode('utf-8'), publicKey)
    return encMessage

def decrypt(encMessage, privateKey):
    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    return decMessage

Alice_publicKey, Alice_privateKey = generate_keys()
Bob_publicKey, Bob_privateKey = generate_keys()
Malice_publicKey, Malice_privateKey = generate_keys()

# A_PK, A_PRK = generate_keys()
# print(A_PK, "\n",A_PRK)
# message = "Hello Bob, I'm Alice"
# encMessage = encrypt(message, A_PK)
# decMessage = decrypt(encMessage, A_PRK)
# print(encMessage, "\n",decMessage)
