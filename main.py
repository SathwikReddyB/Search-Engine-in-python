import string 
import os
from tkinter import Tk, Label, Entry, Button
folder_path = r"C:\Users\hp\Desktop\python search engine\text_files"
file_data = {}
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path , filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding = 'utf-8') as f:
                content = f.read()
                content = content.translate(str.maketrans('','',string.punctuation))
                words = content.split()
                file_data[filename] = {}
                for i in words:
                    if i in file_data[filename]:
                        file_data[filename][i] += 1
                    else:
                        file_data[filename][i] = 1
def querysearch():
        user_input = entry.get()
        results = []
        for fname,freqs in file_data.items():
            if user_input in freqs:
                results.append(f"{fname} : {freqs[user_input]}")
        if results:
            output.config(text="\n".join(results))
        else:
            output.config(text="Word not found in any file")

#front for search engine

root = Tk()
root.title("Search Engine")
root.geometry("500x300")
entry = Entry(root, width=50)
entry.pack(pady=10)
button = Button(root, text="Search", command=querysearch)
button.pack(pady=5)
output = Label(root, text='', width=60, height=10, bg='lightyellow', anchor='nw', justify='left')
output.pack(pady=10, padx=10)
root.mainloop()
