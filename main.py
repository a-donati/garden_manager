# main.py
import tkinter as tk
from views.view import GardenApp 

if __name__ == '__main__':
    root = tk.Tk()  # Initialize the Tkinter root window
    app = GardenApp(root)  # Create an instance of the GardenApp class
    root.mainloop()  # Start the Tkinter main loop
