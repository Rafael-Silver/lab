from tkinter import Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button, END, PhotoImage
import banco as bd

icone_c=(bd.caminho_completo+'icon.png')
tps = None

def get_selecionado(event):
    global tps
    index = lista.curselection()[0]
    tps = lista.get(index)
    entrada_nome.delete(0, END)
    entrada_nome.insert(END, tps[1])
    entrada_endereco.delete(0, END)
    entrada_endereco.insert(END, tps[2])
    entrada_email.delete(0, END)
    entrada_email.insert(END, tps[3])
    entrada_campus.delete(0, END)
    entrada_campus.insert(END, tps[4])
    entrada_periodo.delete(0, END)
    entrada_periodo.insert(END, tps[5])
    entrada_av1.delete(0, END)
    entrada_av1.insert(END, tps[6])
    entrada_av2.delete(0, END)
    entrada_av2.insert(END, tps[7])
    entrada_av3.delete(0, END)
    entrada_av3.insert(END, tps[8])
    entrada_avd.delete(0, END)
    entrada_avd.insert(END, tps[9])
    entrada_avds.delete(0, END)
    entrada_avds.insert(END, tps[10])


def incluir():
    bd.insert(nome.get(), endereco.get(), email.get(), campus.get(), periodo.get(), av1.get(), av2.get(), av3.get(), avd.get(), avds.get())
    lista.delete(0, END)
    lista.insert(END,(nome.get(), endereco.get(), email.get(), campus.get(), periodo.get(), av1.get(), av2.get(), av3.get(), avd.get(), avds.get()))
    entrada_nome.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_email.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    exibir()

def exibir():
    lista.delete(0, END)
    for linha in bd.view():
        lista.insert(0, linha)

def alterar():
    bd.update(tps[0], nome.get(), endereco.get(), email.get(), campus.get(), periodo.get(), av1.get(), av2.get(), av3.get(), avd.get(), avds.get())
    entrada_nome.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_email.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    exibir()

def excluir():
    bd.delete(tps[0])
    entrada_nome.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_email.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    exibir()

root = Tk()
root.title("CADASTRO  DE  ALUNOS")
width = 580
height = 450
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d"%(width, height, x, y))
root.resizable(0,0)
root.iconphoto(True, PhotoImage(file=icone_c))
root.config(bg='gray')

style = ("Calibri", "15", "bold")

label_nome = Label(root, text="Nome:", bg='gray', fg="#ffffff", font=style)
label_nome.grid(row=0, column=0,  padx=(30,0), pady=(15,0))
label_endereco = Label(root, text="Endereço:", bg='gray', fg="#ffffff", font=style)
label_endereco.grid(row=1, column=0,  padx=(30,0))
label_email = Label(root, text="Email:", bg='gray', fg="#ffffff", font=style)
label_email.grid(row=2, column=0,  padx=(30,0))
label_campus = Label(root, text="Campus:", bg='gray', fg="#ffffff", font=style)
label_campus.grid(row=3, column=0,  padx=(30,0))
label_periodo = Label(root, text="Período:", bg='gray', fg="#ffffff", font=style)
label_periodo.grid(row=4, column=0,  padx=(30,0))

entrada_av1 = Label(root, text="AV1:", bg='gray', fg="#ffffff", font=style)
entrada_av1.grid(row=0, column=3, padx=(20,0), pady=(15,0))
entrada_av2 = Label(root, text="AV2:", bg='gray', fg="#ffffff", font=style)
entrada_av2.grid(row=1, column=3, padx=(20,0))
entrada_av3 = Label(root, text="AV3:", bg='gray', fg="#ffffff", font=style)
entrada_av3.grid(row=2, column=3, padx=(20,0))
entrada_avd = Label(root, text="AVD:", bg='gray', fg="#ffffff", font=style)
entrada_avd.grid(row=3, column=3, padx=(20,0))
entrada_avds = Label(root, text="AVDS:", bg='gray', fg="#ffffff", font=style)
entrada_avds.grid(row=4, column=3, padx=(20,0))

nome = StringVar()
endereco = StringVar()
email = StringVar()
campus = StringVar()
periodo = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
avds = StringVar()

entrada_nome = Entry(root,  textvariable=nome, width=30)
entrada_nome.grid(row=0, column=1, columnspan=2, pady=(15,0))
entrada_endereco = Entry(root,  textvariable=endereco, width=30)
entrada_endereco.grid(row=1, column=1, columnspan=2)
entrada_email = Entry(root,  textvariable=email, width=30)
entrada_email.grid(row=2, column=1, columnspan=2)
entrada_campus = Entry(root,  textvariable=campus, width=30)
entrada_campus.grid(row=3, column=1, columnspan=2)
entrada_periodo = Entry(root,  textvariable=periodo, width=6)
entrada_periodo.grid(row=4, column=1, columnspan=1, padx=(0,85))

entrada_av1 = Entry(root,  textvariable=av1, width=5)
entrada_av1.grid(row=0, column=4, padx=(0,1), pady=(15,0))
entrada_av2 = Entry(root,  textvariable=av2, width=5)
entrada_av2.grid(row=1, column=4)
entrada_av3 = Entry(root,  textvariable=av3, width=5)
entrada_av3.grid(row=2, column=4)
entrada_avd = Entry(root,  textvariable=avd, width=5)
entrada_avd.grid(row=3, column=4)
entrada_avds = Entry(root,  textvariable=avds, width=5)
entrada_avds.grid(row=4, column=4)

lista = Listbox(root, height=10, width=63)
lista.grid(row=5, column=0, rowspan=6, columnspan=5,padx=(30,0), pady=(15,0))

sby = Scrollbar(root, orient='vertical', command=lista.yview)
sby.grid(row=5,rowspan=6, column=5, pady=(15,0), sticky='ns')
lista['yscrollcommand']=sby.set

sbx = Scrollbar(root, orient='horizontal', command=lista.xview)
sbx.grid(row=11, columnspan=5, column=0, padx=(30,0), pady=(0,10), sticky='ew')
lista['xscrollcommand']=sbx.set

lista.bind("<<ListboxSelect>>", get_selecionado)

b1 = Button(root, text="Incluir", width=10, bg="light green", command=incluir)
b1.grid(row=12, column=1, pady=(0,5), padx=(0,30))
b2 = Button(root, text="Carregar", width=10, bg="snow", command=exibir)
b2.grid(row=13, column=1, padx=(0,30))
b3 = Button(root, text="Alterar", width=10, bg="light blue", command=alterar)
b3.grid(row=12, column=2, pady=(0,5))
b4 = Button(root, text="Excluir", width=10, bg="OrangeRed2", command=excluir)
b4.grid(row=13, column=2)

root.mainloop()