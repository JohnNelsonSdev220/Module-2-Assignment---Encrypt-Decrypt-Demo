# Module-2-Assignment---Encrypt-Decrypt-Demo

This Python program demonstrates two types of encryption methods:

  Symmetric Encryption- using Fernet cryptography import
  Asymmetric Encryption- using RSA rsa import

The program encrypts and decrypts short messages using both methods and prints the results, including the keys used.

For the Symetric encryption, you set an original message variable, then generate a Fernet key, and set the original message to a new encrypted message variable that uses the Fernet key (fnt.encrypt) to encrypt the original message.
If you want to decrypt it, you simply use the (fnt.decrypt) to decrypt your encrypted message.


For the Asymmetric method, you set public and private to rsa. newkeys, which generates new keys for both private and public.
You then set your original message just like before, and use rsa. encrypt on your original message, followed by the public key.

To decrypt it, you use rsa.decrypt on your encrypted message, followed by your private key.
