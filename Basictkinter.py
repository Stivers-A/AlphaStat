
import tkinter as tk

window = tk.Tk()

window.title('Press a button!')
#the gui is titled Press a button!
greeting = tk.Label(text="Hello, Tkinter")
#creates a label widget with the text Hello, Tkinter assigns it to the vairable greeting
greeting.pack()
#adds the greeting widget to the gui 

button = tk.Button(window, text='Stop', width=25, command=window.destroy)
# command r.destory ends program
button.pack()


window.mainloop()
# mainloop tells python to run the tk main loop, basically stuff after this wont run until the window is closed
print('Hello World')
#this displays in the terminal after the gui is closed