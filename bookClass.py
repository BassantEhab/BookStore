from main import*
class bookclass() :

    NoOfBooks = 0
    RentedBooks = 0

    def __init__(self):
        bookclass.NoOfBooks+=1

    def getBookNo(self,n):
        self.mbookno = n

    def getBookTitle(self, n):
        self.mbooktitle =  n

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
            book.RentedBooks+=1

    def saveData(self):
        bookData = open("bookdata.txt", "a+")
        bookData.write(self.mbookno + "\n")















