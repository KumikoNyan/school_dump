# Revamped with GUI

# libs
from tkinter import *
from tkinter.scrolledtext import * # provides a scroll bar
from tkinter.filedialog import askopenfilename # opening files using windows explorer or file explorers 
from tkinter.font import * # to change the font
# import os.path - for filenotfound

# empty lists that will be appended with values later on
loadIN = []
totalIN = []
invoiceIN = []
sumtotalIN = []
salesrepIN = []

# font for selected GUI
guwifont = ("Cascadia Code", 12)

# to start the GUI
guwi = Tk()
guwi.title("GUI.exe") # title

# text box meant for the transaction button
tb = Entry(guwi, width=20)
tb.grid(row=8, column=1)

# scrollable text box (first box) where the "How to Use?" and price list will appear
tfs = ScrolledText(guwi, width=90, height=10)
# INSERT - index of the insertion cursor, where the text will be placed
tfs.insert(INSERT, '''Welcome to Overpriced Mart ( ง `ω´ )۶! 
\nHow to Use? \n1. Choose a pricelist \n2. Start a transaction by doing (Product ID, Quantity) \n3. Lastly, input a blank to complete the transaction, press "Show Sales Report," and receive your invoice! \nExtras: \n-Use the "Clear" button to remove everything on screen.
-Use the "Undo" button to undo last item you've selected.''')
tfs.grid(row=2, column=0, columnspan=3)

# second scrollable text box (second box) for the outputs
tfs2 = ScrolledText(guwi, width=90, height=10)
tfs2.grid(row=4, column=0, columnspan=3)

# usage is for the "File opened!" message on the top part of the GUI
fstlabel = Label(guwi, text="")
fstlabel.grid(row=1, column=0)

# methods
def setPriceList():
    # removes the root window from the screen without destroying it
    Tk().withdraw()
    # asks the user to locate a file
    filepath = askopenfilename(title = "Select a File")
    loadIN.append(filepath)

    # checks if the file is txt or not
    if filepath.endswith(".txt"):
        with open(filepath, "r+") as tfile: # r+ is simply read and write
            txt = tfile.read()
            tfile.seek(0) # file handle, sets the ref point at the beginning of the file (1 - current, 2 - end) (mainly used for random access reading)
            tfile.truncate() # ability to truncate or resize the file size
            tfile.write(txt.replace(",", "")) # replaces "," with an empty string
    
    # if os.path.isfile(filepath) == True:
        # fstlabel.configure(text = "The File is Opened.", foreground = "blue")

    else:
        # fstlabel.configure(text = "File Not Found/Incompatible File Format", foreground = "red")
        pass

    # returns a str, when file is opened, that has a blue foreground
    fstlabel.configure(text = "The File is Opened.", foreground = "blue")

def printPriceList():
    # clears an entry element
    tfs.delete("0.0", END)
    ploading = loadIN[0] # loads the contents of the list, which is the price list file
    with open(ploading) as price_contents:
        for ele in price_contents:
            ele = ele.replace(",", " ") # formatting, so that it looks presentable on screen
            tfs.insert(INSERT, ele)

def addProductToTransaction(prod, quant):
    # reads and writes tabular data in CSV format (alt for pandas.read_csv)
    import csv
    loading = loadIN[0]

    if loading.endswith(".csv"):
        with open(loading) as csvdata:
            cont = list(csv.reader(csvdata))
            quantity = quant
            prodint = int(prod)
            prodID = (cont[prodint][0]) # product ID
            product = (cont[prodint][1]) # product name
            price = (cont[prodint][2]) # product price
            total = int(price)*int(quantity)
            totalIN.append(int(total)) # added int just to assure
            result = (f"{str(prodID)}\t{str(product)}\t{str(price)}\t{str(quantity)}\t{str(total)}\n")
            invoiceIN.append(result) # append the result (which is a str) to the invoiceIN variable for invoice file usage

    elif loading.endswith(".txt"):
        with open(loading) as txtdata:
            cont = list(csv.reader(txtdata))
            prodint = int(prod)
            txtlist = list(cont[prodint]) # created another list to split in tab spaces, don't want to touch the main file
            for ele in txtlist:
                split = ele.split("\t")

            quantity = quant
            prodID = split[0]
            product = split[1]
            price = split[2]
            total = int(price)*int(quantity)
            totalIN.append(int(total))
            result = (f"{str(prodID)}\t{str(product)}\t{str(price)}\t{str(quantity)}\t{str(total)}\n")
            invoiceIN.append(result)
    
    else:
        pass

def makeNewTransaction():
    y = tb.get() # returns the text box data

    # (product ID, quantity)
    if y != "" or 0:
        y1 = y.split(",")
        y2 = y1[0]
        y3 = y1[1]
        addProductToTransaction(y2,y3)
        showOnScreen()

    else:
        showOnScreen()
        createSalesInvoice()
        salesrepIN.extend(invoiceIN) # .extend extends a list, adds all the elements of an iterable to the end of the list
        sumtotalIN.extend(totalIN)
        invoiceIN.clear()
        totalIN.clear()

def createSalesInvoice():
    fname = "invoice.txt"
    m = invoiceIN
    with open(fname, "a") as contents: # "a" is for appending contents to an existing file (if no file, will create one)
        contents.write("Sales")
        contents.write("ID\tProduct\tPrice\tQuantity\tTotal\n")
        for ele in m:
            contents.write("{}\n".format(ele)) # writes the elements into the file
        contents.write(f"Grand Total: {str(sum(totalIN))}")

# method to show the sales report on the GUI
def salesReport():
    loading3 = loadIN[0]
    tfs2.delete("0.0", END)
    tfs2.insert(INSERT, "Sales Invoice\n")
    tfs2.insert(INSERT, "ID Product Price Quantity Total\n")

    if loading3.endswith(".csv"):
        x = salesrepIN
        for ele in x:
            tfs2.insert(INSERT, ele)
        tfs2.insert(INSERT, f"\n     Grand Total: {str(sum(sumtotalIN))}")

    elif loading3.endswith(".txt"):
        x = salesrepIN
        for ele in x:
            tfs2.insert(INSERT, ele)
        tfs2.insert(INSERT, f"\n     Grand Total: {str(sum(sumtotalIN))}")

    else:
        pass

def showOnScreen():
    loading4 = loadIN[0]
    tfs2.delete("0.0", END)
    tfs2.insert(INSERT, "Sales Invoice\n")
    tfs2.insert(INSERT, "ID Product Price Quantity Total\n")

    if loading4.endswith(".csv"):
        x = invoiceIN
        for ele in x:
            tfs2.insert(INSERT, ele)
        tfs2.insert(INSERT, f"\n     Grand Total: {str(sum(totalIN))}")

    elif loading4.endswith(".txt"):
        x = invoiceIN
        for ele in x:
            tfs2.insert(INSERT, ele)
        tfs2.insert(INSERT, f"\n     Grand Total: {str(sum(totalIN))}")

    else:
        pass

def clearGUI():
    tfs.delete("0.0", END)
    tfs2.delete("0.0", END)
    loadIN.pop(0) # removes the element belonging to an index, in this case 0, which allows us to use another file while the GUI is still running
    setPriceList()
    printPriceList()

def undoRes():
    # simply removes the last invoice and total val from GUI's second terminal
    del invoiceIN[-1]
    del totalIN[-1]
    showOnScreen()

# buttons
button = Button(guwi, text="Set the price list", command=setPriceList)
button1 = Button(guwi, text="Show the price list", command=printPriceList)
button2 = Button(guwi, text="Create a Transaction", command=makeNewTransaction)
button3 = Button(guwi, text="Show Sales Report", command=salesReport)
button4 = Button(guwi, text="Leave Me", command=guwi.destroy) # .destroy basically closes the GUI
button5 = Button(guwi, text="Undo", command=undoRes)
button6 = Button(guwi, text="Clear", command=clearGUI)

# grids for the buttons
button.grid(row=3, column=0)
button1.grid(row=3, column=1)
button2.grid(row=7, column=1)
button3.grid(row=3, column=2)
button4.grid(row=3, column=3)
button5.grid(row=7, column=2)
button6.grid(row=7, column=3)

# runs the event loop
tfs.configure(font=guwifont)
tfs2.configure(font=guwifont)
guwi.mainloop()