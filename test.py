import nonce as nonce
import RSA as RSA
    

# Step 1-3:
print ("Step 1: Alice establish a valid session with Malice\n")
Malice_publicKey, Malice_privateKey = RSA.generate_keys()
print("Alice knows Malice's public key:\n",Malice_publicKey)
Alice_ID = str(input("\nEnter the ID of Alice: "))
NA = nonce.nonceGenerator()
print("\nGennerate Alice's nonce:", NA)
encAliceID = RSA.encrypt(Alice_ID, Malice_publicKey)
encAliceNonce = RSA.encrypt(NA, Malice_publicKey)
print("\nAlice send the message {NA, Alice}KM to Malice:\n", encAliceNonce, encAliceID)

# Step 2-3:
print ("Step 2: Malice decrypt the Alice's message and reencrypt it with Bob's public key\n")
decAliceID = RSA.decrypt(encAliceID , Malice_privateKey)
decAliceNonce = RSA.decrypt(encAliceNonce, Malice_privateKey)
print('\nMalice decrypts the message:', decAliceNonce, decAliceID)
Bob_publicKey, Bob_privateKey= RSA.generate_keys()
print('\nMalice knows Bob\'s public key:\n', Bob_publicKey)
encAliceNonce_MB = RSA.encrypt(decAliceNonce, Bob_publicKey)
encAliceID_MB = RSA.encrypt(decAliceID, Bob_publicKey)
print('\nMalice reencrypts the message with Bob\'s public key:\n', encAliceNonce_MB, encAliceID_MB)

# Step 2-6: 
print("Step 2-6: ")
NB = nonce.nonceGenerator()
print("\nBob's private key:\n", Bob_privateKey)
decNA_B = RSA.decrypt(encAliceNonce_MB, Bob_privateKey)
print("\nBob using his private key to decrypt NA:", decNA_B)
Alice_publicKey, Alice_privateKey = RSA.generate_keys()
print("\nBob responds by picking a new nonce NB:", NB)
encNB = RSA.encrypt(NB, Alice_publicKey) 
encNA = RSA.encrypt(decNA_B, Alice_privateKey)
print("\nBob knows Alice_publicKey is:\n", Alice_publicKey)
print("\nBob use Alice's public key to encrypt NA and NB and try to send it to Alice:\n", encNA, encNB)
print("However, this communication in intercepted by Malice but Malice can not decryt the message because he does not have Alice's private key")

#Step 1-6:
print("Step 1-6:\n")
print('Malice send the message to Alice without doing nothing with it')
print('because he tries to use Alice to execute the decryption for him')

#Step 1-7:
print("Step 1-7:\n")
print("Alice's private key:\n", Alice_privateKey)
decNB = RSA.decrypt(encNB, Alice_privateKey)
print("\nAlice use her private key to decrypt NB:", decNB)
encNB_AM = RSA.encrypt(decNB, Malice_publicKey)
print("\nAlice encrypts NB with Malice's public key and sends it to him:", encNB_AM)

#Step 1-8: 
print("Step 2-7:\n")
print("Malice's private key:\n", Malice_privateKey)
decNB_M = RSA.decrypt(encNB_AM, Malice_privateKey)
print("\nMlice use his private key to decrypt NB:", decNB_M)
encNB_MB = RSA.encrypt(decNB_M, Bob_publicKey)
print("\nAlice encrypts NB with Malice's public key and sends it to him:", encNB_MB)

print('As a result, Bob believes that he is sharing secrets NA, NB with Alice while actually sharing them with Malice.')









