try: # for python2
    import Tkinter as tk
except: #for python3
    import tkinter as tk

class bookstoreApp:

    def __init__(self, master):
        self.master = master
        master.title("Bookstore Management System")
        master.geometry("1000x600")

root = tk.Tk
bookstore = bookstoreApp(root)
root.mainloop()
