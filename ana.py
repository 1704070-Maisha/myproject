import tkinter as tk
root = tk.Tk()
root.geometry('400x400')

def strt():
       label=tk.Label(root,text="hello world")
       label.pack()
def quit():
       label=tk.Label(root,text="bye world").pack()
       root.destroy()
        
        
button1 = tk.Button(root, text = 'Click', command=strt)
button1.pack()
button =tk.Button(root, text = 'Quit', command=quit)
button.pack()
root.mainloop()