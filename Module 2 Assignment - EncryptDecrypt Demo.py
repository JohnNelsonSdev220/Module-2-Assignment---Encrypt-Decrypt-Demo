# symetric Encryption

from cryptography.fernet import Fernet

original_message = "Alexios_Adamenti ACRocks556"

key = Fernet.generate_key()

fnt = Fernet(key)

encrypted_message = fnt.encrypt(original_message.encode())



#Symetric Decrpytion
decrypted_message = fnt.decrypt(encrypted_message).decode()



#asymmetric  Encryption
import rsa

public, private = rsa.newkeys(512)

asymmetric_original_message = "OrignalMessage ThatisNotEncrypted"

asymmetric_encrypted_message = rsa.encrypt(asymmetric_original_message.encode(), public)



#Asymetric Decryption
asymmetric_decrpyted_message = rsa.decrypt(asymmetric_encrypted_message, private).decode()




#Print statements

print("Symmetric key:", key)

print("Public key:", public)
print("Private key:", private)
print("asymmetric decrypted message: ",asymmetric_decrpyted_message)
print("asymmetric encrypted message: ",asymmetric_encrypted_message)
print("symmetric  decrypted message: ", decrypted_message)
print("symmetric  encrypted message: ",encrypted_message)