"""Script to open all the popular 3d model websites in sepearte tabs based on search term input."""

#Import web browser
import webbrowser
#Import Tkinter module
import tkinter as tk
from tkinter import messagebox


#Define a function to get the checkox values printed
def Thingiverse_status():
        print('Thingiverse', var1.get())
def Printables_status():        
        print('Printables', var2.get())
def MakerWorld_status():
       print('MakerWorld', var3.get())
def Yeggi_status():
       print('Yeggi', var4.get())       
def Cults3D_status():
       print('Cults 3D', var5.get())   

#Get the input from the entry box
def get_input():
    term = entry.get()
    print('Input:', term)

#Define the Model search function
def model_search(evet=None):
    search = entry.get().strip()
    if not search:
         #show a message box if the input is empty
         messagebox.showwarning("Input required", "Please enter a search term")
         return
    
    print('searching for:', search)
    
    if var1.get() == 1:
        print('searching thingiverse')
        webbrowser.open(f"https://www.thingiverse.com/search?q={search}")
    if var2.get() == 1:
        print('searching Printables')
        webbrowser.open(f"https://www.printables.com/search/models?q={search}")
    if var3.get() == 1:
        print('Searching MakerWorld')    
        webbrowser.open(f"https://makerworld.com/en/search/models?keyword={search}")
    if var4.get() == 1:
        print('Searching Yeggi')    
        webbrowser.open(f"https://www.yeggi.com/q/{search}/")
    if var5.get() == 1:
        print('Searching Cults 3d')    
        webbrowser.open(f"https://cults3d.com/en/search?q={search}")

#Create root TK window
window=tk.Tk()

#Root window title and dimensions
window.title('3D Print Fetcher')

#Set geometry
window.geometry('400x300')

#Set prompt on root window
lbl = tk.Label(window, text = 'What model would you like to search for?')
lbl.grid(row=1, column=1)

#Create input box
var_entry = tk.StringVar()
entry = tk.Entry(window, textvariable = var_entry)
entry.grid(row=2, column=1)

#Button Widget
btn = tk.Button(window, text = 'Search', command = lambda: [get_input(), model_search()]) 
btn.grid(row=3, column=1)

#Bind enter to search button
entry.bind('<Return>', model_search)

#Creates check boxes for what sites to search
var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(window, text = 'Thingiverse', variable=var1, onvalue = 1, offvalue = 0,command = Thingiverse_status)
checkbox1.grid(row=4, column=0,  sticky='w')

var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(window, text = 'Printables', variable=var2, onvalue = 1, offvalue = 0,command = Printables_status)
checkbox2.grid(row=5, column=0,  sticky='w')

var3 = tk.IntVar()
checkbox3 = tk.Checkbutton(window, text = 'MakerWorld', variable=var3, onvalue = 1, offvalue = 0,command = MakerWorld_status)
checkbox3.grid(row=6, column=0, sticky='w')

var4 = tk.IntVar()
checkbox4 = tk.Checkbutton(window, text = 'Yeggi', variable=var4, onvalue = 1, offvalue = 0,command = Yeggi_status)
checkbox4.grid(row=7, column=0, sticky='w')

var5 = tk.IntVar()
checkbox5 = tk.Checkbutton(window, text = 'Cults 3D', variable=var5, onvalue = 1, offvalue = 0,command = Cults3D_status)
checkbox5.grid(row=8, column=0, sticky='w')


#Execute TKinter
window.mainloop()



