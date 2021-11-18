from alunos import Alunos
from tkinter import Frame,END,INSERT,Button,LEFT,RIGHT,Label,Entry, Text, Scrollbar

class Application:
    
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 5
        self.container10.pack()


        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidaluno = Label(self.container2,
        text="idAluno:", font=self.fonte, width=10)
        self.lblidaluno.pack(side=LEFT)

        self.txtidaluno = Entry(self.container2)
        self.txtidaluno["width"] = 10
        self.txtidaluno["font"] = self.fonte
        self.txtidaluno.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarAluno
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblendereco = Label(self.container4, text="Endereço:",
        font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)

        self.txtendereco = Entry(self.container4)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblperiodo= Label(self.container6, text="Período:",
        font=self.fonte, width=10)
        self.lblperiodo.pack(side=LEFT)

        self.txtperiodo = Entry(self.container6)
        self.txtperiodo["width"] = 25
        self.txtperiodo["font"] = self.fonte
        self.txtperiodo.pack(side=LEFT)

        self.lblcampus= Label(self.container7, text="Campus:",
        font=self.fonte, width=10)
        self.lblcampus.pack(side=LEFT)

        self.txtcampus = Entry(self.container7)
        self.txtcampus["width"] = 25        
        self.txtcampus["font"] = self.fonte
        self.txtcampus.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirAluno
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarAluno
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirAluno
        self.bntExcluir.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Listar todos",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.buscarTodosAlunos
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.lblmsg2 = Label(self.container10, text="")
        self.lblmsg2["font"] = ("Verdana", "9", "italic")
        self.lblmsg2.pack()

        # Create the text widget
        self.text_widget = Text(master, height=5, width=40)

        # Create a scrollbar
        self.scroll_bar = Scrollbar(master)

        # Pack the scroll bar
        # Place it to the right side, using tk.RIGHT
        self.scroll_bar.pack(side= RIGHT)

        # Pack it into our tkinter application
        # Place the text widget to the left side
        self.text_widget.pack(side= LEFT)

        long_text = ""

        #text_widget.insert(END, long_text)

    def inserirAluno(self):
        user = Alunos()

        user.nome = self.txtnome.get()
        user.endereco = self.txtendereco.get()
        user.email = self.txtemail.get()
        user.periodo = self.txtperiodo.get()
        user.campus = self.txtcampus.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcampus.delete(0, END)



    def alterarAluno(self):
        user = Alunos()

        user.idaluno = self.txtidaluno.get()
        user.nome = self.txtnome.get()
        user.endereco = self.txtendereco.get()
        user.email = self.txtemail.get()
        user.periodo = self.txtperiodo.get()
        user.campus = self.txtcampus.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcampus.delete(0, END)



    def excluirAluno(self):
        user = Alunos()

        user.idaluno = self.txtidaluno.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidaluno.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcampus.delete(0, END)


    def buscarAluno(self):
        user = Alunos()

        idaluno = self.txtidaluno.get()

        self.lblmsg["text"] = user.selectUser(idaluno)

        self.txtidaluno.delete(0, END)
        self.txtidaluno.insert(INSERT, user.idaluno)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT,user.endereco)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtperiodo.delete(0, END)
        self.txtperiodo.insert(INSERT, user.periodo)

        self.txtcampus.delete(0, END)
        self.txtcampus.insert(INSERT,user.campus)

    def buscarTodosAlunos(self):
        user = Alunos()

        #self.lblmsg2["text"] = user.selectAllUsers()
        listagemDeAlunos = user.selectAllUsers()
        self.text_widget.insert(END, listagemDeAlunos)
