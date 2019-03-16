from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def file_open():
    root.filename = filedialog.askopenfilename(initialdir='/python', title="Select file",
                                           filetypes=[("Text Files", "*.txt")])
    f = open(str(root.filename), 'r')
    input_text_area.delete('1.0', END)
    input_text_area.insert(CURRENT, f.read())

def file_new():
    input_text_area.delete('1.0', END)

def help_about():
    messagebox.showinfo("About", "This text editor was created by soneill and uses the tkinter library for python.")


def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = str(input_text_area.get(1.0, END))
    f.write(text2save)
    f.close()

ON
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

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=help_about)
menubar.add_cascade(label="Help", menu=helpmenu)

input_text_area = Text(root)
input_text_area.grid(row=1, column=0, columnspan=4, sticky=W+E)
input_text_area.pack(expand=True, fill='both')
input_text_area.configure(background='white', fg='black')
input_text_area.bind("<Control-Key-a>", select_all)
input_text_area.bind("<Control-Key-A>", select_all)


root.config(menu=menubar)

root.grid_columnconfigure(0, weight=1)
root.geometry("500x500")
img = PhotoImage(file='soneillz.png')
root.title("soneillz Text-Editor")
try:
    root.call('wm', 'iconphoto', root._w, img)
    root.mainloop()
except TclError:
    pass
root.mainloop()
