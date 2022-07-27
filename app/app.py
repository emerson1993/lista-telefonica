from tkinter import *
import mysql.connector

### CONEXÃO COM O DATABASE:
con = mysql.connector.connect(host='localhost',database='ListaTelefonicaDB',user='root',password='')
cursor = con.cursor()

### DEF DA JANELA ADD CONTATOS:
def new_contact():
    def add_contact():
        name = str(inboxname.get())
        phone = str(inboxphone.get())


        insert_data = '\''+ name +'\','+ phone +')'

        insert_data_table = """INSERT INTO tbl_ContactList
                                            (ContactName, PhoneNumber)
                                            VALUES ("""

        SQL = insert_data_table + insert_data
        print(SQL)

        cursor.execute(SQL)
        con.commit()

    def return_window():
        AddContactWindow.destroy()

### JANELA ADICIONAR CONTATO:        
    AddContactWindow = Toplevel(root)
    AddContactWindow.geometry("400x267")
    AddContactWindow.resizable(0,0)
    AddContactWindow.title("Add new contact.")
    AddContactWindow.configure(background='#F5F5F5')
    #AddContactWindow.iconbitmap("24hrs.ico")

    ##BACKGROUNDIMAGE##
    bckimg = PhotoImage(file= r'addnewcontact.png')
    background_label = Label(AddContactWindow, image=bckimg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    ##INBOX##
    inboxname = StringVar()
    inboxnameBox = Entry(AddContactWindow, textvariable=inboxname)
    inboxnameBox.place(x=104, y=109, height=30, width=200)

    inboxphone = StringVar()
    inboxphoneBox = Entry(AddContactWindow, textvariable=inboxphone)
    inboxphoneBox.place(x=108, y=184, height=30, width=150)
    ##BUTTONS##
    AddContactButton = PhotoImage(file='addcontact.png')
    Button_img_add = Label(image=AddContactButton)
    button = Button(AddContactWindow, image=AddContactButton,command=add_contact,borderwidth=0)
    button.place(x=290, y=210)

    ReturnButton = PhotoImage(file='return.png')
    Button_img_return = Label(image=ReturnButton)
    button= Button(AddContactWindow, image=ReturnButton,command=return_window,borderwidth=0)
    button.place(x=355, y=7)

    AddContactWindow.mainloop()

### DEF DA JANELA PESQUISAR CONTATOS:
def SearchContact():
    def SearchName():        
        search = str(inboxsearch.get())
        
        consulta_sql = "SELECT * FROM tbl_ContactList WHERE ContactName="'\''+search+'\''";"
        
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print("Total number of records returned: ",cursor.rowcount)

        print("\nShow register products\n")

        for linha in linhas:
            text = Label(SearchContactWindow, text="Code: ",bg='#AFABAB', font=("Arial", 12, "bold"),fg="#000000", cursor="hand2")
            text.place(x=15,y=160)
            text = Label(SearchContactWindow, text=linha[0],bg='#AFABAB', font=("Arial", 12, "bold"),fg="#000000", cursor="hand2")
            text.place(x=70,y=160)

            text = Label(SearchContactWindow, text="Name: ",bg='#AFABAB', font=("Arial", 12, "bold"), fg="#000000", cursor="hand2")
            text.place(x=15,y=185)
            text = Label(SearchContactWindow, text=linha[1],bg='#AFABAB', font=("Arial", 12, "bold"), fg="#000000", cursor="hand2")
            text.place(x=70,y=185)

            text = Label(SearchContactWindow, text="Phone: ",bg='#AFABAB', font=("Arial", 12, "bold"), fg="#000000", cursor="hand2")
            text.place(x=12,y=215)
            text = Label(SearchContactWindow, text=linha[2],bg='#AFABAB', font=("Arial", 12, "bold"), fg="#000000", cursor="hand2")
            text.place(x=70,y=215)
            
    def return_window():
        SearchContactWindow.destroy()

### JANELA PESQUISAR CONTATOS:        
    SearchContactWindow = Toplevel(root)
    SearchContactWindow.geometry("401x308")
    SearchContactWindow.resizable(0,0)
    SearchContactWindow.title("Search contact.")
    SearchContactWindow.configure(background='#F5F5F5')
    #SearchContactWindow.iconbitmap("24hrs.ico")

    ##BACKGROUNDIMAGE##
    bckimg = PhotoImage(file= r'searchcontact.png')
    background_label = Label(SearchContactWindow, image=bckimg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    ##INBOX##
    inboxsearch = StringVar()
    inboxsearchBox = Entry(SearchContactWindow, textvariable=inboxsearch)
    inboxsearchBox.place(x=50, y=70, height=40, width=300)

    ##BUTTONS##
    SearchContactButton = PhotoImage(file='search.png')
    Button_img_add = Label(image=SearchContactButton)
    button = Button(SearchContactWindow, image=SearchContactButton,command=SearchName,borderwidth=0)
    button.place(x=160, y=115)

    ReturnButton = PhotoImage(file='return.png')
    Button_img_return = Label(image=ReturnButton)
    button= Button(SearchContactWindow, image=ReturnButton,command=return_window,borderwidth=0)
    button.place(x=355, y=10)

    SearchContactWindow.mainloop()
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada.")

### DEF DA JANELA PRINCIPAL:        
def finalizar():
    if messagebox.askokcancel("Shutting Down...","continue?"):
        root.destroy()

def sair(event):
    finalizar()

### JANELA PRINCIPAL:
root = Tk()
root.geometry("380x443")
root.resizable(0,0)
root.title("Phone List")
root.configure(background='#F5F5F5')
#root.iconbitmap(".ico")

##BACKGROUNDIMAGE##
bckimg = PhotoImage(file= r'ListInCloud.png')
background_label = Label(root, image=bckimg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

##BUTTONS##
NewContactButton = PhotoImage(file='add_contact.png')
Button_img_new = Label(image=NewContactButton)
button = Button(root, image=NewContactButton,command=new_contact,borderwidth=0)
button.place(x=35, y=200)

SearchButton = PhotoImage(file='searchbutton.png')
Button_img_search = Label(image=SearchButton)
button= Button(root, image=SearchButton,command=SearchContact,borderwidth=0)
button.place(x=35, y=300)

root.mainloop()

### FINALIZANDO CONEXÃO COM O BD:
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada.")
