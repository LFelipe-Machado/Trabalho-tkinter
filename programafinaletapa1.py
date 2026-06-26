from tkinter import *
from tkinter import colorchooser

figuras = []
figuranova = None

cor_borda = '#000000'
cor_preenchimento = '#ffffff'

# Programa Principal
janela = Tk()
janela.title('Projeto Felipe e Ranieri Tkinter')
janela.geometry('1024x576')

tipofigura_var = StringVar(janela)

# Fazer a área de desenho crescer se mudar a geometria da janela
janela.columnconfigure(1, weight=1)
janela.rowconfigure(9, weight=1)

#seletor de cor
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
    posicao = (event.x, event.y, event.x, event.y)

    if tipo == 'Linha':
        figuranova = ('linha', posicao, cor_borda)
    elif tipo == 'Rabisco':
        figuranova = ('rabisco', [(event.x, event.y)], cor_borda)
    elif tipo == 'Retângulo':
        figuranova = ('retangulo', posicao, cor_borda, cor_preenchimento)
    elif tipo == 'Oval':
        figuranova = ('oval', posicao, cor_borda, cor_preenchimento)
    elif tipo == 'Círculo':
        figuranova = ('circulo', posicao, cor_borda, cor_preenchimento)

def atualizar_figuranova(event):
    global figuranova

    if figuranova is None:
        return
    
    tipo = figuranova[0]

    if tipo == 'rabisco':
        figuranova[1].append((event.x, event.y))
        desenhar_figuras()
        desenhar_figuranova()
        return
    
    x0, y0 = figuranova[1][0], figuranova[1][1]

    if tipo == 'linha':
        figuranova = ('linha', (x0, y0, event.x, event.y), figuranova[2])
    elif tipo == 'retangulo':
        figuranova = ('retangulo', (x0, y0, event.x, event.y), figuranova[2], figuranova[3])
    elif tipo == 'oval':
        figuranova = ('oval', (x0, y0, event.x, event.y), figuranova[2], figuranova[3])
    elif tipo == 'circulo':
        lado = min(abs(event.x - x0), abs(event.y - y0))
        x1 = x0 + (lado if event.x >= x0 else -lado)
        y1 = y0 + (lado if event.y >= y0 else -lado)
        figuranova = ('circulo', (x0, y0, x1, y1), figuranova[2], figuranova[3])

    desenhar_figuras()
    desenhar_figuranova()

def incluir_figuranova(event):
    if figuranova is not None and not incompleta(figuranova):
        figuras.append(figuranova)
        
    desenhar_figuras()

# Funcões de desenho

def incompleta(figura):
    tipo = figura[0]
    valores = figura[1]
    if tipo == 'rabisco':
        return len(valores) <= 1
    return (valores[0], valores[1]) == (valores[2], valores[3])

def desenhar_figuras():
    areadesenho.delete('all')
    for figura in figuras:
        _desenhar(figura)

def desenhar_figuranova():
    _desenhar(figuranova, dash=(4, 2))

def _desenhar(figura, dash=()):
    tipo = figura[0]
    valores = figura[1]
    borda = figura[2] if len(figura) > 2 else 'black'
    fill  = figura[3] if len(figura) > 3 else ''

    if tipo == 'linha':
        areadesenho.create_line(valores[0], valores[1], valores[2], valores[3], fill=borda, dash=dash)
    elif tipo == 'rabisco':
        if len(valores) >= 2:
            areadesenho.create_line(valores, fill=borda, dash=dash, smooth=True)
    elif tipo == 'retangulo':
        areadesenho.create_rectangle(valores[0], valores[1], valores[2], valores[3], outline=borda, fill=fill, dash=dash)
    elif tipo in ('oval', 'circulo'):
        areadesenho.create_oval(valores[0], valores[1], valores[2], valores[3], outline=borda, fill=fill, dash=dash)

# Esquerda
Label(janela,
      text='Forma').grid(row=0,
                         column=0,
                         padx=12,
                         pady=6,
                         sticky=NW)

OptionMenu(janela,
           tipofigura_var,
           'Linha',
           'Rabisco',
           'Retângulo',
           'Oval',
           'Círculo').grid(row=1,
                           column=0,
                           padx=12,
                           sticky=NW)

Label(janela, text='Borda:').grid(row=2, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_borda = Button(janela, text='     ', bg=cor_borda,
                       command=escolher_cor_borda, relief=RIDGE)
btn_cor_borda.grid(row=3, column=0, padx=12, sticky=NW)

Label(janela, text='Preenchimento:').grid(row=4, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_preench = Button(janela, text='     ', bg=cor_preenchimento,
                         command=escolher_cor_preenchimento, relief=RIDGE)
btn_cor_preench.grid(row=5, column=0, padx=12, sticky=NW)

# Direita
areadesenho = Canvas(janela,
                     bg='white')
areadesenho.grid(row=0,
                 column=1,
                 rowspan=10,
                 padx=12,
                 pady=6,
                 sticky=NSEW)  

areadesenho.bind('<ButtonPress-1>', iniciar_figuranova)
areadesenho.bind('<B1-Motion>', atualizar_figuranova)
areadesenho.bind('<ButtonRelease-1>', incluir_figuranova)

janela.mainloop()