from tkinter import *
import RSA as RSA
import nonce as nonce

window = Tk()

window.title("Demo App: Step 1-3")

window.geometry('1800x400')

# step13_label = Label(window, text="Step 1-3:", font=("Arials", 16))
# step13_label.grid(column=0, row=0)
def step13():
    AID = "Alice123"
    def AliceID():
        res_show = Label(window, text="Alice's ID:")
        res_show.grid(column=2, row=2)
        res_NA_label = Label(window)
        res_NA_label.grid(column=3, row=2)
        res_NA_label.configure(text= AID)
    AID_button = Button(window, text="Show Alice's Identity", command=AliceID)
    AID_button.grid(column=0, row=2)

    NA = nonce.nonceGenerator()
    def nonce_NA():
       res_show = Label(window, text="NA:")
       res_show.grid(column=2, row=3)
       res_NA_label = Label(window)
       res_NA_label.grid(column=3, row=3)
       res_NA_label.configure(text=NA)
    NA_button = Button(window, text="Gennerate Alice's nonce", command=nonce_NA)
    NA_button.grid(column=0, row=3)
    
    def malicePublicKey():
        res_show = Label(window, text="Malice's public key:")
        res_show.grid(column=2, row=4)
        res_NA_label = Label(window)
        res_NA_label.grid(column=3, row=4)
        res_NA_label.configure(text=RSA.Malice_publicKey)
        
    MPK_button = Button(window, text="Alice knows Malice's public key", command=malicePublicKey)
    MPK_button.grid(column=0, row=4)
    
    label1 = Label(window, text="Alice encrypts her nonce and her ID with Malice's public key")
    label1.grid(column=0, row=5)
    
    encryptedAID = RSA.encrypt(AID, RSA.Malice_publicKey)
    def decryptAID():
        res_show = Label(window, text="Encrypted AID:")
        res_show.grid(column=2, row=6)
        res_NA_label = Label(window)
        res_NA_label.grid(column=3, row=6)
        res_NA_label.configure(text=encryptedAID)
        
    decAID_button = Button(window, text="Alice encrypts her ID", command=decryptAID)
    decAID_button.grid(column=0, row=6)
    
    encryptedNA = RSA.encrypt(NA, RSA.Malice_publicKey)
    def decryptNA():
        res_show = Label(window, text="Encrypted NA:")
        res_show.grid(column=2, row=7)
        res_NA_label = Label(window)
        res_NA_label.grid(column=3, row=7)
        res_NA_label.configure(text=encryptedNA)
    decNA_button = Button(window, text="Alice encrypts NA", command=decryptNA)
    decNA_button.grid(column=0, row=7)
    
    label1 = Label(window, text="Alice sends her message including both encrypted NA and ID to Malice")
    label1.grid(column=0, row=8)

    def step23():
        newWindow = Tk()
        newWindow.title("Demo App: Step 2-3")
        newWindow.geometry('1800x400')

        label1 = Label(newWindow, text = 'Malice decrypts Alice\'s ID to verify her identity')
        label1.grid(column = 0, row = 0)
        M_privatekey = RSA.Malice_privateKey

        decryptedAID = RSA.decrypt(encryptedAID, M_privatekey)
        def decryptAID():
            res_show = Label(newWindow, text ="Alice's ID:")
            res_show.grid(column = 1, row = 2)
            res_NA_label = Label(newWindow)
            res_NA_label.grid(column=2, row=2)
            res_NA_label.configure(text = decryptedAID)  
        decAID_button = Button(newWindow, text="Malice decrypts Alice's ID", command = decryptAID)
        decAID_button.grid(column = 0, row =2)

        decryptedNA = RSA.decrypt(encryptedNA, M_privatekey)
        def decryptNA():
            res_show = Label(newWindow, text ="NA:")
            res_show.grid(column = 1, row = 3)
            res_NA_label = Label(newWindow)
            res_NA_label.grid(column=2, row=3)
            res_NA_label.configure(text = decryptedNA)  
        decNA_button = Button(newWindow, text="Malice decrypts Alice's Nonce", command = decryptNA)
        decNA_button.grid(column = 0, row =3)
        
        def showBobPublicKey():
            res_show = Label(newWindow, text ='Bob\'s Public Key:')
            res_show.grid(column = 1, row = 4)
            res_NA_label = Label(newWindow)
            res_NA_label.grid(column = 2, row = 4)
            res_NA_label.configure(text = RSA.Bob_publicKey)
        showMPrK_button = Button(newWindow, text = 'Malice knows Bob\'s Public Key', command=showBobPublicKey)
        showMPrK_button.grid(column =0, row = 4)

        encryptedAID_B = RSA.encrypt(decryptedAID, RSA.Bob_publicKey)
        def encryptAID_B():
            res_show = Label(newWindow, text ='Encrypted Alice\'s ID:')
            res_show.grid(column = 1, row = 5)
            res_NA_label = Label(newWindow)
            res_NA_label.grid(column = 2, row = 5)
            res_NA_label.configure(text = encryptedAID_B)
        showMPrK_button = Button(newWindow, text = 'Malice encrypts Alice\'s ID with Bob\'s public key', command=encryptAID_B)
        showMPrK_button.grid(column =0, row = 5)

        encryptedNA_B = RSA.encrypt(decryptedNA, RSA.Bob_publicKey)
        def encryptNA_B():
            res_show = Label(newWindow, text ='Encrypted NA:')
            res_show.grid(column = 1, row =6)
            res_NA_label = Label(newWindow)
            res_NA_label.grid(column = 2, row = 6)
            res_NA_label.configure(text = encryptedNA_B)
        showMPrK_button = Button(newWindow, text = 'Malice encrypts NA with Bob\'s public key', command=encryptNA_B)
        showMPrK_button.grid(column =0, row = 6)

        label2 = Label(newWindow, text = 'Malice sends NA and Alice\'s ID, which are encrypted with Bob\'s public key to Bob')
        label2.grid(column = 0, row = 7)

        def step26():
            newWindow1 = Tk()
            newWindow1.title("Demo App: Step 2-6")
            newWindow1.geometry('1800x400')

            label3 = Label(newWindow1, text = 'Bob decrypts Alice\'s ID and NA using his private key')
            label3.grid(column = 0, row = 0)

            decryptedAID_B = RSA.decrypt(encryptedAID_B, RSA.Bob_privateKey)
            def decrypt_AID():
                res_show = Label(newWindow1, text ="Alice's ID:")
                res_show.grid(column = 1, row = 1)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=1)
                res_NA_label.configure(text = decryptedAID_B)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Bob decrypts Alice's ID", command = decrypt_AID)
            decrypt_NA_Bob_button.grid(column = 0, row =1)

            label4 = Label(newWindow1, text = '=>> After verifying, Bob thinks that he truely communicate with Alice')
            label4.grid(column = 0, row = 2)

            decryptedNA_B = RSA.decrypt(encryptedNA_B, RSA.Bob_privateKey)
            def decrypt_NA():
                res_show = Label(newWindow1, text ="NA:")
                res_show.grid(column = 1, row = 3)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=3)
                res_NA_label.configure(text = decryptedNA_B)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Bob decrypts Alice's Nonce", command = decrypt_NA)
            decrypt_NA_Bob_button.grid(column = 0, row =3)

            NB = nonce.nonceGenerator()
            def nonce_NB():
                res_show = Label(newWindow1, text ="NB:")
                res_show.grid(column = 1, row = 4)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=4)
                res_NA_label.configure(text = NB)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Gennerate Bob's Nonce", command = nonce_NB)
            decrypt_NA_Bob_button.grid(column = 0, row =4)

            def publicKey_A():
                res_show = Label(newWindow1, text ="Alice's public key: ")
                res_show.grid(column = 1, row = 5)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=5)
                res_NA_label.configure(text = RSA.Alice_publicKey)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Bob knows Alice's public key", command = publicKey_A)
            decrypt_NA_Bob_button.grid(column = 0, row =5)
            
            label5 = Label(newWindow1, text = "=>> Bob uses Alice's public key to encrypt NA and NB")
            label5.grid(column = 0, row = 6)

            encryptedNA_A = RSA.encrypt(decryptedNA_B, RSA.Alice_publicKey)
            def encryptNA_A():
                res_show = Label(newWindow1, text ="Encrypted NA:")
                res_show.grid(column = 1, row = 7)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=7)
                res_NA_label.configure(text = encryptedNA_A)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Bob encrypts NA", command = encryptNA_A)
            decrypt_NA_Bob_button.grid(column = 0, row =7)
            
            encryptedNB_A = RSA.encrypt(NB, RSA.Alice_publicKey)
            def encryptNB_A():
                res_show = Label(newWindow1, text ="Encrypted NB:")
                res_show.grid(column = 1, row = 8)
                res_NA_label = Label(newWindow1)
                res_NA_label.grid(column=2, row=8)
                res_NA_label.configure(text = encryptedNB_A)  
            decrypt_NA_Bob_button = Button(newWindow1, text="Bob encrypts NB", command = encryptNB_A)
            decrypt_NA_Bob_button.grid(column = 0, row =8)

            label6 = Label(newWindow1, text = "=>> Bob sends encrypted NA and NB to Alice")
            label6.grid(column = 0, row = 9)

            def step16():
                newWindow2 = Tk()
                newWindow2.title("Demo App: Step 1-6")
                newWindow2.geometry('1800x400')
                
                label7 = Label(newWindow2, text = "Malice intercepts the communication between Alice and Bob\n but he can't decrypt it since he doesn't have Alice's private key")
                label7.grid(column = 0, row = 0)

                label7 = Label(newWindow2, text = "=> Malice sends the message to Alice to use her to decrypt it for him")
                label7.grid(column = 0, row = 1)

                
                def step17():
                    newWindow3 = Tk()
                    newWindow3.title("Demo App: Step 1-7")
                    newWindow3.geometry('1800x400')
                    
                    label7 = Label(newWindow3, text = "Alice uses her private key to decrypt the message")
                    label7.grid(column = 0, row = 0)

    
                    decryptedNB_A = RSA.decrypt(encryptedNB_A, RSA.Alice_privateKey)
                    def decryptNB_A():
                        res_show = Label(newWindow3, text ="NB:")
                        res_show.grid(column = 1, row = 1)
                        res_NA_label = Label(newWindow3)
                        res_NA_label.grid(column=2, row=1)
                        res_NA_label.configure(text = decryptedNB_A)  
                    decrypt_NA_Bob_button = Button(newWindow3, text="Alice decrypts NB", command = decryptNB_A)
                    decrypt_NA_Bob_button.grid(column = 0, row =1)

                    label8 = Label(newWindow3, text = "Alice uses Malice's public key to encrypt NB and send it to him")
                    label8.grid(column = 0, row = 2)

                    encryptedNB_M = RSA.encrypt(decryptedNB_A, RSA.Malice_publicKey)
                    def encryptNB_M():
                        res_show = Label(newWindow3, text ="Encrypted NB:")
                        res_show.grid(column = 1, row = 3)
                        res_NA_label = Label(newWindow3)
                        res_NA_label.grid(column=2, row=3)
                        res_NA_label.configure(text = encryptedNB_M)  
                    decrypt_NA_Bob_button = Button(newWindow3, text="Alice encrypts NB", command = encryptNB_M)
                    decrypt_NA_Bob_button.grid(column = 0, row =3)

                    def step27():
                        newWindow4 = Tk()
                        newWindow4.title("Demo App: Step 2-7")
                        newWindow4.geometry('1800x400')
                    
                        label9 = Label(newWindow4, text = "Malice uses his private key to dencrypt the message")
                        label9.grid(column = 0, row = 0)

                        decryptedNB_M = RSA.decrypt(encryptedNB_M, RSA.Malice_privateKey)
                        def decryptNB_M():
                            res_show = Label(newWindow4, text ="NB:")
                            res_show.grid(column = 1, row = 1)
                            res_NA_label = Label(newWindow4)
                            res_NA_label.grid(column=2, row=1)
                            res_NA_label.configure(text = decryptedNB_M)  
                        decrypt_NA_Bob_button = Button(newWindow4, text="Malice decrypts NB", command = decryptNB_M)
                        decrypt_NA_Bob_button.grid(column = 0, row =1)

                        label10 = Label(newWindow4, text = "Malice uses Bob's public key to encrypt NB and send it to him")
                        label10.grid(column = 0, row = 2)

                        encryptedNB_B = RSA.encrypt(decryptedNB_A, RSA.Malice_publicKey)
                        def encryptNB_B():
                            res_show = Label(newWindow4, text ="Encrypted NB:")
                            res_show.grid(column = 1, row = 3)
                            res_NA_label = Label(newWindow4)
                            res_NA_label.grid(column=2, row=3)
                            res_NA_label.configure(text = encryptedNB_B)  
                        decrypt_NA_Bob_button = Button(newWindow4, text="Malice encrypts NB", command = encryptNB_B)
                        decrypt_NA_Bob_button.grid(column = 0, row =3)

                        label11 = Label(newWindow4, text = "=> As a result, Bob believes that he is sharing secrets NA, NB with Alice while actually sharing them with Malice")
                        label11.grid(column = 0, row = 4)

                    step27_button = Button(newWindow3, text="Next: Step 2-7", command=step27)
                    step27_button.grid(column=0, row = 4)       

                step17_button = Button(newWindow2, text="Next: Step 1-7", command=step17)
                step17_button.grid(column=0, row = 2)       
        
            step16_button = Button(newWindow1, text="Next: Step 1-6", command=step16)
            step16_button.grid(column=0, row = 10)

        step26_button = Button(newWindow, text="Next: Step 2-6", command=step26)
        step26_button.grid(column=0, row = 8)

    step23_button = Button(window, text="Next: Step 2-3", command=step23)
    step23_button.grid(column=0, row = 9)

label12 = Label(window, text="Follow step by step:")
label12.grid(column=0, row =0)
step13_button = Button(window, text="Step 1-3", command=step13 )
step13_button.grid(column=0, row=1)

    
            








window.mainloop()
