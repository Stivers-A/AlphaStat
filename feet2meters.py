from tkinter import *
from tkinter import ttk
# * adds tkinter
# tkk adds new widgets
# using tkdocs first example
root = Tk()
root.title("Feet to Meters")
#this sets up the application window and names it.

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
#this actually does the feet to meter conversion,  its encased in a try catch to ensure the user only enters numbers
#then it converts the value of feet to a float from a string, then sets the value of meters and accounts for float rounding errors by dividing & multiplying by 10,000


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#This is a frame widget named mainframe
#as the root isnt a themed widget but the frame is this causes the asthetics to be consistent in the background and foreground
#grid sets up a structure to place future widgets
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
#first creates a string for feet, then creates an entry text box that assigns its input to feet

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#the next 5 widgets include the label for the meters conversion and the button to trigger the conversion and 3 static text labels to explain what to do.


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)
#this part adds some polish,it adds padding to all child widgets within mainframe widget.
# .focus() places the cursor at the feet entry point 
#.bind <return> makes hitting return call caclulate like hitting the calculate button

root.mainloop()

