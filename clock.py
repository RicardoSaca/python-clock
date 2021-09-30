from tkinter import Tk, Label, mainloop, BOTTOM
from time import strftime

root = Tk()
root.geometry("300x150")
root.resizable(0,0)
root.title('Python Clock')
root.configure(background='black')

Label(root, text='Python Clock', font='arial 20 bold',fg='white', background='black').pack(side=BOTTOM)

def time():
    string = strftime('%a %b %-m\n%I:%M:%S %p')
    mark.config(text=string)
    mark.after(1000, time)

mark = Label(root,
            font = ('calibiri', 40,'bold'),
            pady=150,
            background='black',
            foreground= 'cyan')

mark.pack(anchor='center')
time()

mainloop()