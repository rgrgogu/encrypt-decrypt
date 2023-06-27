import hashlib                      # library for SHA 256 (creating a SHA-256 object)
import base64                       # library used to encode and decode data in a format
from Crypto import Random           # generate random numbers from Crypto library (creating initialization vector or AES Cipher)
from Crypto.Cipher import AES       # library that provides the AES cipher, which is a powerful encryption algorithm.

BS = 16  # block size for the AES Cipher (16 byte - common value for many encryption algorithms)

# pad = function that returns a padded string, makes that the encrypted data is a multiple of the block size
# done by appending the string with the character chr(BS - len(s) % BS) repeated as many times as necessary to 
# make the length of the string a multiple of the block size
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')  

# unpad = function that takes padded string and returns the unpadded string.
# done by removing the last byte from the string,
# truncating the string to the next multiple or the block size
unpad = lambda s : s[0:-ord(s[-1:])]

# Cipher = class contains the encrypt and decrypt function
class Cipher:
    # Constructor
    # Initialize the key 
    def __init__( self, key ):
        # key = argument value
        # self.key = hashed key of encoded key argument from the input string
        # works in bytes not strings
        self.key = hashlib.sha256(key.encode("utf-8")).digest()

    # Method that takes the raw data as the input string
    # Returns the encrypted data as a base64-encoded string which is byte type
    # CBC mode is a secure encryption mode that is used to encrypt data blocks. 
    # The IV is used to ensure that the encryption of each block is independent 
    # of the encryption of the previous blocks.
    def encrypt( self, raw ):
        # This ensures that the encrypted data is a multiple of the block size.
        raw = pad(raw)                                    
        # Generates a random 16-byte initialization vector (IV). The IV is used to encrypt the data.   
        iv = Random.new().read( AES.block_size)  
        # Creates a new AES cipher object using the key and the IV.
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Encrypts the padded data using the cipher object and 
        # base64-encodes the encrypted data and returns it.
        return base64.b64encode( iv + cipher.encrypt( raw ))

    # Method that takes the encrypted data as input and 
    # returns the decrypted data as a string.
    # Same with encryption, the decrypt function uses CBC mode in AES Cipher and IV purpose.
    def decrypt( self, enc ):
        # Decodes the encrypted data from base64.
        enc = base64.b64decode(enc)
        # Extracts the IV from the encrypted data.
        iv = enc[:16]
        # Creates a new AES cipher object using the key and the IV.
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Decrypts the encrypted data using the cipher object and decodes the decrypted data 
        # from bytes to string using UTF-8 format.

        return unpad(cipher.decrypt( enc[16:] )).decode('utf-8')