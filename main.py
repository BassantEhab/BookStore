import tkinter as tk
from tkinter import*
#from bookClass import*

#-------------------------------------------------------------------------------------------------#
class bookclass() :

    NoOfBooks = 0
    RentedBooks = 0

    def __init__(self):
        bookclass.NoOfBooks += 1

    def getBookNo(self,n):
        self.mbookno = n

    def getBookTitle(self, n):
        self.mbooktitle = n

    def getBookCategory(self,n):
        self.mcategory = n

    def getBookPublication(self , n):
        self.mpublication = n

    def getBookPages(self , n):
        self.mpages = n

    def getBookPrice(self , n):
        self.mpages = n

    def getBookStock(self , n):
        self.mstock = n

    #it recieves a value from a radio button
    def isRented(self, n):
        self.mrented = n
        if n == 2:
            bookclass.RentedBooks+=1

    def saveData(self):
        bookData = open("bookdata.txt", "a+")
        print("i am hell there!!!!!!!")
        print(self.mbookno)
        bookData.write(self.mbookno + "\n")
        bookData.write("hi there" + "\n")
        bookData.close()
#-------------------------------------------------------------------------------------------------#

window = tk.Tk()
window.title('Bookstore management system')
window.geometry("1000x600")

#-------------------------------------------------------------------------------------------------#Frames

topFrame = tk.Frame(master = window , height = 100 )
topFrame.pack(fill=X)

menuFrame = tk.Frame(master= window , width = 150, bg="#e06a38")
menuFrame.pack(fill=Y , side=LEFT)

mainFrame = tk.Frame(master=window,width=850 )
mainFrame.pack(side=LEFT, fill=tk.BOTH)

#-------------------------------------------------------------------------------------------------#functions

bookData = open("bookdata.txt" , "w+")
bookData.write("book no \t book title \t category \t author name \t publication \t no of pages \t price \t stock \t status \n")
ButtonSelected = 0
fields = 'bookNo' , 'bookName' , 'category' , 'authorName' , 'publication' , 'numberOfPages' , 'price' , 'stock'
entries = []

def deleteWidget():
    for widget in mainFrame.winfo_children():
        widget.destroy()
        #widget.delete()

def disableButton(btnName):
    btnName.config(state=DISABLED)

def enableButton(btnName):
    btnName.config(state=NORMAL)

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()

def addFn():
    instance = bookclass()
    instance.mbookno = StringVar()
    disableButton(addBook)

    title = Label(master=mainFrame, text="add book details:")
    title.config(font=("Sans-serif" , 16 , 'bold'))
    title.grid(row=0 , column = 0)
    title.pack(padx=15, pady=9)

    bookNo= Label(mainFrame , text="Book No.: ")
    bookNo_entry= Entry(mainFrame )
    bookNo.pack()
    bookNo_entry.pack()
    instance.getBookNo(bookNo_entry.get())
    print(bookNo_entry.get())

    bookTitle = Label(mainFrame , text="Book Title:")
    bookTitle_entry = Entry(mainFrame)
    bookTitle.pack()
    bookTitle_entry.pack()

    category=Label(mainFrame , text="Category:")
    category.pack()
    var1 = tk.StringVar()
    drop = tk.OptionMenu(mainFrame ,var1 , 'fiction' , 'crime' , 'comedy','romance','literature' )
    drop.pack()

    authorName = Label(mainFrame , text = "Author Name:")
    authorName.pack()
    authorName_entry = Entry(mainFrame)
    authorName_entry.pack()

    publication = Label(mainFrame , text="Publication:")
    publication.pack()
    publication_entry = Entry(mainFrame)
    publication_entry.pack()

    pages = Label(mainFrame , text="No. of Pages:")
    pages.pack()
    pages_entry = Entry(mainFrame)
    pages_entry.pack()

    price = Label(mainFrame , text="Price:")
    price.pack()
    price_entry = Entry(mainFrame)
    price_entry.pack()

    stock = Label(mainFrame , text="Stock:")
    stock.pack()
    stock_entry = Entry(mainFrame)
    stock_entry.pack()

    saveButton = Button(mainFrame , text="Save" , width=10, command = lambda:saveBookData(instance))
    saveButton.pack()

def saveBookData(instance):
    addBook.config(state=NORMAL)
    deleteWidget()
    instance.saveData()
    #addFn()

bookData.close()

#-------------------------------------------------------------------------------------------------#Buttons

label = Label(master = topFrame  , text = "Bookstore management system",bg="#2b2e33", fg = "#f45009" )
label.config(font=("Courier" ,28))
label.pack(fill=X)

#........Dashboard button......

photo_1 = PhotoImage(file="home.png")
dashboard = Button(master=menuFrame , text = "  Dahsboard "  , height = 50 ,width=150, bg="#9b4925", borderwidth=0,compound=LEFT )
dashboard.config(image=photo_1, font=("Sans-serif" ,13), anchor="w")
dashboard.pack()

#........add button......

photo2=PhotoImage(file="add.png" )
addBook = Button(master=menuFrame , text="  add book", height= 50,width=150, bg="#a84f28", borderwidth=0,compound=LEFT ,command=addFn)
addBook.config(image=photo2 , font=("Sans-serif" , 13), anchor="w")
addBook.pack()

#........search button......

photo4 = PhotoImage(file="search.png")
searchBook = Button(master=menuFrame , text="  Search", height= 50,width=150, bg="#b7562c", borderwidth=0,compound=LEFT)
searchBook.config(image=photo4 , font = ("Sans-serif" , 13), anchor="w")
searchBook.pack()

#........order button......

photo5 = PhotoImage(file="delivery.png")
order = Button(master=menuFrame , text="  Order", height= 50,width=150, bg="#ce6233", borderwidth=0,compound=LEFT )
order.config(image=photo5 , font = ("Sans-serif" , 13) , anchor="w")
order.pack()

#........rent button......

photo6 = PhotoImage(file="rent.png")
rent = Button(master=menuFrame , text="  Rent ", height= 50,width=150, bg="#e06a38", borderwidth=0,compound=LEFT )
rent.config(image=photo6 , font = ("Sans-serif" , 13) , anchor="w")
rent.pack()

#-------------------------------------------------------------------------------------------------#

window.mainloop()





