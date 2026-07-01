from tkinter import *
from tkinter import colorchooser
from classespt2 import *

figuras = []
figuranova = None

cor_borda = '#000000'
cor_preenchimento = '#ffffff'

# Programa Principal
janela = Tk()
janela.title('Projeto Felipe e Ranieri Tkinter')
janela.geometry('1024x576')

tipofigura_var = StringVar(janela)

janela.columnconfigure(1, weight=1)
janela.rowconfigure(9, weight=1)

# Funções de cor
def escolher_cor_borda():
    global cor_borda
    cor = colorchooser.askcolor(title='Cor da borda', color=cor_borda)
    if cor[1]:
        cor_borda = cor[1]
        btn_cor_borda.config(bg=cor_borda)

def escolher_cor_preenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor(title='Cor de preenchimento', color=cor_preenchimento)
    if cor[1]:
        cor_preenchimento = cor[1]
        btn_cor_preench.config(bg=cor_preenchimento)

# Funções do mouse
def iniciar_figuranova(event):
    global figuranova
    tipo = tipofigura_var.get()

    if tipo == 'Polígono' and figuranova is not None:
        figuranova.adicionar_ponto(event.x, event.y)
        desenhar_figuras()
        desenhar_figuranova()
        return

    if tipo == 'Linha':
        figuranova = Linha(event.x, event.y, cor_borda)
    elif tipo == 'Rabisco':
        figuranova = Rabisco(event.x, event.y, cor_borda)
    elif tipo == 'Retângulo':
        figuranova = Retangulo(event.x, event.y, cor_borda, cor_preenchimento)
    elif tipo == 'Oval':
        figuranova = Oval(event.x, event.y, cor_borda, cor_preenchimento)
    elif tipo == 'Círculo':
        figuranova = Circulo(event.x, event.y, cor_borda, cor_preenchimento)
    elif tipo == 'Polígono':
        figuranova = Poligono(event.x, event.y, cor_borda, cor_preenchimento)

def atualizar_figuranova(event):
    if figuranova is None:
        return

    tipo = tipofigura_var.get()

    if tipo == 'Rabisco':
        figuranova.adicionar_ponto(event.x, event.y)
    elif tipo == 'Polígono':
        desenhar_figuras()
        desenhar_figuranova()
        ultimo = figuranova.pontos[-1]
        areadesenho.create_line(ultimo[0], ultimo[1], event.x, event.y,
                                fill=figuranova.cor_borda, dash=(4, 2))
        return
    else:
        figuranova.atualizar(event.x, event.y)

    desenhar_figuras()
    desenhar_figuranova()

def incluir_figuranova(event):
    global figuranova
    if tipofigura_var.get() == 'Polígono':
        return
    if figuranova is not None and not figuranova.incompleta():
        figuras.append(figuranova)
        figuranova = None
    desenhar_figuras()

def finalizar_poligono(event):
    global figuranova
    if figuranova is not None and not figuranova.incompleta():
        figuras.append(figuranova)
        figuranova = None
    desenhar_figuras()

# Funções de desenho
def desenhar_figuras():
    areadesenho.delete('all')
    for figura in figuras:
        figura.desenhar(areadesenho)

def desenhar_figuranova():
    if figuranova is not None:
        figuranova.desenhar(areadesenho, dash=(4, 2))

# Esquerda
Label(janela,
      text='Forma').grid(row=0, column=0, padx=12, pady=6, sticky=NW)

OptionMenu(janela,
           tipofigura_var,
           'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo', 'Polígono'
           ).grid(row=1, column=0, padx=12, sticky=NW)

Label(janela, text='Borda:').grid(row=2, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_borda = Button(janela, text='     ', bg=cor_borda,
                       command=escolher_cor_borda, relief=RIDGE)
btn_cor_borda.grid(row=3, column=0, padx=12, sticky=NW)

Label(janela, text='Preenchimento:').grid(row=4, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_preench = Button(janela, text='     ', bg=cor_preenchimento,
                         command=escolher_cor_preenchimento, relief=RIDGE)
btn_cor_preench.grid(row=5, column=0, padx=12, sticky=NW)

# Direita
areadesenho = Canvas(janela, bg='white')
areadesenho.grid(row=0, column=1, rowspan=10, padx=12, pady=6, sticky=NSEW)

areadesenho.bind('<ButtonPress-1>',   iniciar_figuranova)
areadesenho.bind('<B1-Motion>',       atualizar_figuranova)
areadesenho.bind('<ButtonRelease-1>', incluir_figuranova)
areadesenho.bind('<ButtonPress-3>',   finalizar_poligono)

janela.mainloop()
