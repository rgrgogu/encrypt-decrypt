from Cipher import Cipher   # import Cipher class from Cipher.py

# The function displays a menu of options and prompts the user to choose an option.
# :return: The function `option()` returns an integer value that represents the user's choice from the
# menu options displayed.

def option():
    menu_options = {
        1: 'Encrypt file',
        2: 'Decrypt file',
        3: 'Exit'
    }

    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
    
    return int(input('Enter your choice: '))


# This function prompts the user to enter a filename and returns the input concatenated with a given
# string.

# :param str: a string that describes the action the user is taking with the filename
# :return:  user input for the filename

def read_filename(str):
    return input('Enter the filename you want to ' + str + ': ')


# This function reads a file, encrypts its contents using a given cipher, and writes the encrypted
# data to a new file.

# :param cipher: The cipher object that will be used to encrypt the data in the input file. It is
# assumed that this object has already been initialized with a key and other necessary parameters

def process_encrypt(cipher):
    arr = read(read_filename("encrypt"), 'r')
    encrypted_arr = []

    for item in arr:
        encrypted_arr.append(cipher.encrypt(item))

    write(encrypted_arr, 'Encrypted.txt')


# This function takes a cipher and uses it to decrypt a file, then writes the decrypted data to a new
# file.

# :param cipher: The cipher object that will be used to encrypt the data in the input file. It is
# assumed that this object has already been initialized with a key and other necessary parameters

def process_decrypt(cipher):
    arr = read(read_filename("decrypt"), 'rb')
    decrypted_arr = []

    for item in arr:
        decrypted_arr.append(cipher.decrypt(item))

    write(decrypted_arr, 'Decrypted.txt')

# The function takes a choice and a cipher as input and performs encryption or decryption based on the
# choice.

# :param choice: an integer representing the user's choice of operation (1 for encryption, 2 for
# decryption, 3 for exit)
# :param cipher: The cipher parameter is a object containing the key

def process(choice, cipher):
    if choice == 1:
        process_encrypt(cipher)
    elif choice == 2:
        process_decrypt(cipher)
    elif choice == 3:
        return
    else:
        print('Invalid Input! Please try again!')

# This function reads a file and returns its contents as a list of strings or bytes depending on the
# specified mode.

# :param filename: The name or path of the file to be read
# :param mode: The mode parameter specifies the mode in which the file is opened. It can be 'r' for
# reading in text mode or 'rb' for reading in binary mode
# :return: a list of lines read from the file specified by the filename argument. The mode argument
# specifies the mode in which the file is opened ('r' for text mode or any other mode for binary
# mode). If an error occurs while reading the file, the function prints the error message.

def read(filename, mode):
    try:
        if mode == 'r':
            with open(filename, mode) as reader:
                return reader.read().split('\n')
        else:
            with open(filename, mode) as reader:
                return reader.read().split(b'\n')
            
    except Exception as err:
        print(err)


# The function writes data to a file and handles encryption for a specific file name.

# :param arr: an array of data to be written to a file
# :param filename: The name of the file to be written to

def write(arr, filename):
    try:
        if filename == 'Encrypted.txt':
            with open(filename, 'wb') as writer:
                for item in arr:
                    if item == arr[-1]:
                        writer.write(item)
                    else:
                        writer.write(item + b'\n')
        else:
            with open(filename, 'w') as writer:
                for item in arr:
                    if item == arr[-1]:
                        writer.write(item)
                    else:
                        writer.write(item + '\n')
        
        str = "encrypted" if filename == "Encrypted.txt" else "decrypted"
        print('Data has been ' + str + ' and exported!\n')
    except Exception as err:
        print(err)

choice = 1
cipher = Cipher('secret')

while choice != 3:
    choice = option()
    process(choice, cipher)

print("\nProgram Terminated!")