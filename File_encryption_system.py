from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    text_file = fd.askopenfilename(title = "Open text file", filetypes = (("Text Files", "*.txt"),))
    print(text_file)
    paragraph = open(text_file, 'r')
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    print(file_hexd)
    md5_file = open("md5.txt", 'w')
    md5_file.write(file_hexd)
    print(file_hexd)
    md5_file.close()
    
def apply_sha256():
    text_file2 = fd.askopenfilename(title = "Open text file", filetypes = (("Text Files", "*.txt"),))
    print(text_file2)
    paragraph2 = open(text_file2, 'r')
    file_result2 = hashlib.sha256(paragraph2.encode())
    file_hexd2 = file_result2.hexdigest()
    print(file_hexd2)
    sha256_file = open("sha256.txt", 'w')
    sha256_file.write(file_hexd2)
    print(file_hexd2)
    sha256_file.close()    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()