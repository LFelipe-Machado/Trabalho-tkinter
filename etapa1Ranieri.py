from tkinter import colorchooser


#cor borda e preenchimento
cor_borda = '#000000'
cor_preenchimento = '#ffffff'


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

#novo botao
Label(janela, text='Borda:').grid(row=2, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_borda = Button(janela, text='     ', bg=cor_borda,
                       command=escolher_cor_borda, relief=RIDGE)
btn_cor_borda.grid(row=3, column=0, padx=12, sticky=NW)

Label(janela, text='Preenchimento:').grid(row=4, column=0, padx=12, pady=(12, 0), sticky=NW)
btn_cor_preench = Button(janela, text='     ', bg=cor_preenchimento,
                         command=escolher_cor_preenchimento, relief=RIDGE)
btn_cor_preench.grid(row=5, column=0, padx=12, sticky=NW)
