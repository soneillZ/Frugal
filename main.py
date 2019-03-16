from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

def font_size():
    answer = simpledialog.askstring("Font Size", "Enter font size.",
    parent=root)
    input_text_area.configure(background='white', fg='black', font=("Arial", int(answer), "bold"))


def file_open():
    root.filename = filedialog.askopenfilename(initialdir='/python', title="Select file",
                                           filetypes=[("Text Files", "*.txt")])
    f = open(str(root.filename), 'r')
    input_text_area.delete('1.0', END)
    input_text_area.insert(CURRENT, f.read())

def file_new():
    input_text_area.delete('1.0', END)

def help_about():
    messagebox.showinfo("About Frugal",
    '''Made for Windows and Linux operating systems\nVersion 0.3 (Windows build v0.2)\n\nCopyright (c) 2019 Sean O'Neill
    ''')


def file_save():
    f = filedialog.asksaveasfile(title="Save File", mode='w', defaultextension=".txt")
    if f is None:
        return
    text_save = str(input_text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def file_savebind(self):
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if f is None:
        return
    text_save = str(input_text_area.get(1.0, END))
    f.write(text_save)
    f.close()


def select_all(event):
    input_text_area.tag_add(SEL, "1.0", END)
    input_text_area.mark_set(INSERT, "1.0")
    input_text_area.see(INSERT)
    return 'break'

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=file_new)
filemenu.add_command(label="Open", command=file_open)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Font Size", command=font_size)
menubar.add_cascade(label="Tools", menu=toolsmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=help_about)
menubar.add_cascade(label="Help", menu=helpmenu)

input_text_area = Text(root)
input_text_area.grid(row=1, column=0, columnspan=4, sticky=W+E)
input_text_area.pack(expand=True, fill='both')
input_text_area.configure(background='white', fg='black', font=("Calibri", 13))
input_text_area.bind("<Control-Key-a>", select_all)
input_text_area.bind("<Control-Key-A>", select_all)
input_text_area.bind("<Control-Key-s>", file_savebind)
input_text_area.bind("<Control-Key-S>", file_savebind)


root.config(menu=menubar)

yscrollbar=Scrollbar(root, orient=VERTICAL, command=input_text_area.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
input_text_area["yscrollcommand"]=yscrollbar.set
input_text_area.pack(side=LEFT, fill=BOTH, expand = YES)
root.grid_columnconfigure(0, weight=1)
img = PhotoImage(file='icon.png')
root.title("Frugal")
try:
    root.call('wm', 'iconphoto', root._w, img)
    root.mainloop()
except:
    pass
root.mainloop()