"""
Utilizamos neste código as bibliotecas tkinter e mysql.connector.
"""
from tkinter import *
from tkinter import messagebox
import mysql.connector

"""
Começamos informando as credenciais de acesso ao banco de dados que será utilizado no ListaTelefonica.py
"""
con = mysql.connector.connect(host='localhost',database='ListaTelefonicaDB',user='root',password='')
cursor = con.cursor()

def new_contact():
    """
    Está função irá chamar uma nova janela ao ListaTelefonica.py chamada new_contact.
    Nela serão informados os dados do novo contato.
    """

    def add_contact():
        """
        Está função enviará os dados informados pelo usuário ao banco de dados vinculado.
        """
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
        """
        Utilizamos está função para destruir a janela em destaque, retornando para a principal.
        """

        AddContactWindow.destroy()

    """
    A seguir, primeiro criamos a janela AddContactWindow e adicionamos os dados das informações da janela
    a dimensão, icone, título, cor, imagem de fundo e sua posição na tela.
    """
        
    AddContactWindow = Toplevel(root)
    AddContactWindow.geometry("400x267")
    AddContactWindow.resizable(0,0)
    AddContactWindow.title("Add new contact.")
    AddContactWindow.configure(background='#F5F5F5')
    #AddContactWindow.iconbitmap("24hrs.ico")

    bckimg = PhotoImage(file= r'addnewcontact.png')
    background_label = Label(AddContactWindow, image=bckimg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    """
    Adicionando as caixas editáveis que conterão a informação de nome e o número do novo contato.
    """
    inboxname = StringVar()
    inboxnameBox = Entry(AddContactWindow, textvariable=inboxname)
    inboxnameBox.place(x=104, y=109, height=30, width=200)

    inboxphone = StringVar()
    inboxphoneBox = Entry(AddContactWindow, textvariable=inboxphone)
    inboxphoneBox.place(x=108, y=184, height=30, width=150)
    
    """
    Dois botões criados para que a função add_contact e return_window sejam chamadas
    quando clicados pelo usuário.
    """
    AddContactButton = PhotoImage(file='addcontact.png')
    Button_img_add = Label(image=AddContactButton)
    button = Button(AddContactWindow, image=AddContactButton,command=add_contact,borderwidth=0)
    button.place(x=290, y=210)

    ReturnButton = PhotoImage(file='return.png')
    Button_img_return = Label(image=ReturnButton)
    button= Button(AddContactWindow, image=ReturnButton,command=return_window,borderwidth=0)
    button.place(x=355, y=7)

    AddContactWindow.mainloop()

def SearchContact():
    """
    Nesta função a janela SearchContactWindow é criada para que o usuário possa procurar
    um contato específico.
    """
    def SearchName():
        """
        Está função SearchName busca as informações no banco de dados para exxibir
        na tela se o contato for encontrado.
        """     
        search = str(inboxsearch.get())
        
        consulta_sql = "SELECT * FROM tbl_ContactList WHERE ContactName="'\''+search+'\''";"
        
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        """
        Aqui retornamos na tela os dados encontrados da pesquisa utilizando for.
        """
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
        """
        Utilizamos está função para destruir a janela em destaque, retornando para a principal.
        """
        SearchContactWindow.destroy()

    """
    A seguir, primeiro criamos a janela SearchContactWindow e adicionamos os dados das informações da janela
    a dimensão, icone, título, cor, imagem de fundo e sua posição na tela.
    """
    SearchContactWindow = Toplevel(root)
    SearchContactWindow.geometry("401x308")
    SearchContactWindow.resizable(0,0)
    SearchContactWindow.title("Search contact.")
    SearchContactWindow.configure(background='#F5F5F5')
    #SearchContactWindow.iconbitmap("24hrs.ico")

    bckimg = PhotoImage(file= r'searchcontact.png')
    background_label = Label(SearchContactWindow, image=bckimg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    """
    Adicionando a caixa editável que contém a informação do nome que será pesquisado.
    """
    inboxsearch = StringVar()
    inboxsearchBox = Entry(SearchContactWindow, textvariable=inboxsearch)
    inboxsearchBox.place(x=50, y=70, height=40, width=300)

    """
    Dois botões criados para que a função SearchName e return_window sejam chamadas
    quando clicados pelo usuário.
    """
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
      
def finalizar():
    """
    Está função finliza a janela principal.
    """
    if messagebox.askokcancel("Shutting Down...","continue?"):
        root.destroy()

def sair(event):
    """
    Chama a função finalizar.
    """
    finalizar()

"""
A seguir, primeiro criamos a janela root e adicionamos os dados das informações da janela
a dimensão, icone, título, cor, imagem de fundo e sua posição na tela.
"""
root = Tk()
root.geometry("380x443")
root.resizable(0,0)
root.title("Phone List")
root.configure(background='#F5F5F5')
#root.iconbitmap(".ico")

bckimg = PhotoImage(file= r'ListInCloud.png')
background_label = Label(root, image=bckimg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
"""
Dois botões criados para que a função NewContactButton e SearchButton sejam chamadas
quando clicados pelo usuário.
"""
NewContactButton = PhotoImage(file='add_contact.png')
Button_img_new = Label(image=NewContactButton)
button = Button(root, image=NewContactButton,command=new_contact,borderwidth=0)
button.place(x=35, y=200)

SearchButton = PhotoImage(file='searchbutton.png')
Button_img_search = Label(image=SearchButton)
button= Button(root, image=SearchButton,command=SearchContact,borderwidth=0)
button.place(x=35, y=300)

root.mainloop()
"""
Finaliza a conexão com o servidor.
"""
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada.")