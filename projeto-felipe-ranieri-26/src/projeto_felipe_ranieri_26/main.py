from tkinter import Tk
from visao.visao import Visao
from modelo.figuras import Desenho
from controlador.controlador import Controlador

janela = Tk()
visao = Visao(janela)
desenho = Desenho()
controlador = Controlador(visao, desenho)
janela.mainloop()
