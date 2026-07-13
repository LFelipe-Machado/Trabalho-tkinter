"""
@package main
@brief Ponto de entrada do sistema de desenho Tkinter.

Inicializa a janela, cria as instâncias de Visao, Desenho e Controlador
e inicia o loop principal da aplicação.

@author Felipe Machado e Ranieri Pereira
@version 2.0
@since 2026-07-08
"""

from tkinter import Tk
from visao.visao import Visao
from modelo.figuras import Desenho
from controlador.controlador import Controlador

janela = Tk()
visao = Visao(janela)
desenho = Desenho()
controlador = Controlador(visao, desenho)
janela.mainloop()
