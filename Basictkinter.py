
import tkinter as tk

window = tk.Tk()

window.title('Press a button!')

#the gui is titled Press a button!
greeting = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="#34A2FE",  # Set the background color to light blue using Hexadecimal
    height=10
    #if no units are set height and length are set in text units, meaning just like text charaters they are taller than they are long
)
#creates a label widget with the text Hello, Tkinter assigns it to the vairable greeting
greeting.pack()
#adds the greeting widget to the gui 

button = tk.Button(
    window,
    text='Stop',
    bg="grey",
    fg="yellow",
    #bg is shorthamd for background, fg is shorthand for forground 
    width=25,
    command=window.destroy)
# command r.destory ends program
button.pack()

#The entry widget allows for more complex user input than a button
#this label renders right above the input acting like a descriptor
entryLabel = tk.Label(
    text="Labels allow for text input",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entryLabel.pack()
entry.pack()
#entry.get can be used to retrieve user inputs from entry
window.mainloop()
# mainloop tells python to run the tk main loop, basically stuff after this wont run until the window is closed
print('Hello World')
#this displays in the terminal after the gui is closed