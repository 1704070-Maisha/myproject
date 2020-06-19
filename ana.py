import tkinter as tk
root = tk.Tk()
root.geometry('400x4000')

def strt():
       label=tk.Label(root,text="hello")
       label.pack()
def quit():
       root.destroy()
        
        
button1 = tk.Button(root, text = 'Click', command=strt)
button1.pack()
button =tk.Button(root, text = 'Quit', command=quit)
button.pack()
root.mainloop()
