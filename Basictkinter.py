
import tkinter as tk

r = tk.Tk()
r.title('Press a button!')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# command r.destory ends program
button.pack()
r.mainloop()