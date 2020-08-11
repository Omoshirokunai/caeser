from tkinter import *
import tkinter.font as tkFont
import collections
import string
##--Application by muhsin Hameed--##
#Our GUI Window
window = Tk()
window.title("cipherAPP")
width=600
height=500
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)

#labels
ft = tkFont.Font(family='Times',size=10)
messagelabel=Label(window,font=ft,justify="center",text="Message")
messagelabel.place(x=0,y=40,width=97,height=44)

shiftlabel=Label(window,font=ft,justify="center",text="Shift")
shiftlabel.place(x=10,y=110,width=70,height=25)

#Enter Message
yourMessage=Entry(window,font=ft,justify="left",text="Message")
yourMessage.place(x=80,y=50,width=381,height=30)

#Enter Shifts
def showpass() : #for security we hide the shift key/encryption key
    if var.get() == 1 :
        Cshifts.configure(show = "")
    elif var.get() == 0 :
        Cshifts.configure(show = "*")
var = IntVar()  

Cshifts=Entry(window,font=ft,justify="left",text="Shifts",show="*")
Cshifts.place(x=80,y=100,width=83,height=30)
bt = Checkbutton(window, command = showpass, offvalue = 0, onvalue = 1, variable = var)
bt.place(x = 155, y = 100)

#Radiobutton for encrypt and decryption
encORdec = IntVar()
Radiobutton(window, text="encrypt", variable=encORdec, value=1).pack(anchor=W)
Radiobutton(window, text="Decrypt", variable=encORdec, value=2).pack(anchor=W)


def cipher():
    x = yourMessage.get()
    x = x.lower()
    alphabet = collections.deque(string.ascii_lowercase) # queue of letters in the alphabet
    try:
        shift = int(Cshifts.get())
    except:
        output.configure(text="Sorry shift Operator ONLY takes integers values", font=("Courier", 10))
    else:
        alphabet.rotate(shift)
        alphabet = "".join(list(alphabet))
        if encORdec.get()==1:
            encrypted = x.translate(str.maketrans(string.ascii_lowercase,alphabet)) #maps the lettters to our shifted alphabet
            output.configure(text="Your Encrypted message is: {}".format(encrypted))
        
        if encORdec.get()==2:
            decrypted = x.translate(str.maketrans(alphabet,string.ascii_lowercase)) 
            output.configure(text="Your Decrypted message is: {}".format(decrypted))



#output box
output=Label(window,font=ft,justify="center",text=" ")
output.place(x=90,y=250,width=441,height=195)
#button to encrypt or decrypt
run=Button(window,text="Run cipher",command=cipher,bg= "#f0f0f0",font=ft,justify="center")
run.place(x=230,y=110,width=141,height=30)
window.mainloop()