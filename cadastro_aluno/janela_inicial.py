from tkinter import Tk
from menu import Application

###############CONFIGURAÇÕES DA  JANELA##################################
menu_inicial = Tk()
menu_inicial.title("Sistema de Notas")
menu_inicial.geometry("500x600+0+0")
menu_inicial.resizable(False, False)
#menu_inicial.minsize(500,250)
#menu_inicial.maxsize(700,400)
#menu_inicial.state("zoomed")
#menu_inicial.iconbitmap("images/icon.ico")
Application(menu_inicial)
menu_inicial.mainloop()
#########################################################################