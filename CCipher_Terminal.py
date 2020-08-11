import collections
import string
##--Application by muhsin Hameed--##

message = str(input("enter a string: "))
while True:
    try:
        shifts = int(input("input a shift number: "))   
    except ValueError:
        print("Invalid input")
    else:
        break
encryptORdecrypt = str(input("Encrypt(e) or Decrypt(D):")).lower()
# encryptORdecrypt = encryptORdecrypt[0]
print(encryptORdecrypt[0])
def cipher(mes,shift,enordec):
    alphabet = collections.deque(string.ascii_lowercase) # queue of letters in the alphabet
    alphabet.rotate(shift)
    alphabet = "".join(list(alphabet))
    
    if enordec[0] == 'e':
        encrypted = mes.translate(str.maketrans(string.ascii_lowercase,alphabet)) #maps the lettters to our shifted alphabet
        print("your encrypted message is: "+encrypted)
    elif enordec[0] == 'd':
        decrypted = mes.translate(str.maketrans(alphabet,string.ascii_lowercase)) 
        print("your decrypted message is: "+decrypted)
    else:
        print("invalid operation")
        print(encryptORdecrypt[0])
        
cipher(message,1,encryptORdecrypt)    



