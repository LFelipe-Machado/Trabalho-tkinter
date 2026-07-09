from tkinter import *
from tkinter import colorchooser

class Visao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Projeto Felipe e Ranieri Tkinter')
        self.janela.geometry('1024x576')
        self.tipofigura_var = StringVar(janela)
        self.cor_borda = '#000000'
        self.cor_preenchimento = '#ffffff'
        self.janela.columnconfigure(1, weight=1)
        self.janela.rowconfigure(9, weight=1)
        self._criar_widgets()

    def _criar_widgets(self):
        Label(self.janela, text='Forma').grid(row=0, column=0, padx=12, pady=6, sticky=NW)
        OptionMenu(self.janela, self.tipofigura_var,
                   'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo', 'Polígono'
                   ).grid(row=1, column=0, padx=12, sticky=NW)
        Label(self.janela, text='Borda:').grid(row=2, column=0, padx=12, pady=(12,0), sticky=NW)
        self.btn_cor_borda = Button(self.janela, text='     ', bg=self.cor_borda,
                                    command=self.escolher_cor_borda, relief=RIDGE)
        self.btn_cor_borda.grid(row=3, column=0, padx=12, sticky=NW)
        Label(self.janela, text='Preenchimento:').grid(row=4, column=0, padx=12, pady=(12,0), sticky=NW)
        self.btn_cor_preench = Button(self.janela, text='     ', bg=self.cor_preenchimento,
                                      command=self.escolher_cor_preenchimento, relief=RIDGE)
        self.btn_cor_preench.grid(row=5, column=0, padx=12, sticky=NW)
        self.areadesenho = Canvas(self.janela, bg='white')
        self.areadesenho.grid(row=0, column=1, rowspan=10, padx=12, pady=6, sticky=NSEW)

    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title='Cor da borda', color=self.cor_borda)
        if cor[1]:
            self.cor_borda = cor[1]
            self.btn_cor_borda.config(bg=self.cor_borda)

    def escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor(title='Cor de preenchimento', color=self.cor_preenchimento)
        if cor[1]:
            self.cor_preenchimento = cor[1]
            self.btn_cor_preench.config(bg=self.cor_preenchimento)

    def desenhar_figuras(self, figuras):
        self.areadesenho.delete('all')
        for figura in figuras:
            figura.desenhar(self.areadesenho)

    def desenhar_figuranova(self, figuranova):
        if figuranova is not None:
            figuranova.desenhar(self.areadesenho, dash=(4, 2))
