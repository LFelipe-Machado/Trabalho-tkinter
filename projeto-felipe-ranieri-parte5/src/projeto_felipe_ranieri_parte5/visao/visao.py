"""
@package visao.visao
@brief Módulo contendo a classe de visão do padrão MVC.
@author Felipe Machado e Ranieri Pereira
@version 2.0
@since 2026-07-08
"""

from tkinter import *
from tkinter import colorchooser, filedialog


class Visao:
    """
    @brief Classe responsável pela interface gráfica do sistema de desenho.

    Implementa a camada de Visão do padrão MVC, criando e gerenciando
    todos os widgets tkinter: janela, canvas, menu, botões e labels.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-08
    """

    def __init__(self, janela):
        """
        @brief Inicializa a visão configurando a janela e criando os widgets.
        @param janela: Janela principal tkinter.
        @type janela: tkinter.Tk
        """
        self.janela = janela
        self.janela.title('Projeto Felipe e Ranieri Tkinter')
        self.janela.geometry('1024x576')

        self.tipofigura_var = StringVar(janela)
        self.cor_borda = '#000000'
        self.cor_preenchimento = '#ffffff'

        self.janela.columnconfigure(1, weight=1)
        self.janela.rowconfigure(9, weight=1)

        self._criar_menu()
        self._criar_widgets()

    def _criar_menu(self):
        """
        @brief Cria a barra de menu com as opções Arquivo > Salvar e Abrir.
        """
        menubar = Menu(self.janela)
        menu_arquivo = Menu(menubar, tearoff=0)
        menu_arquivo.add_command(label='Abrir', command=self.pedir_caminho_abrir)
        menu_arquivo.add_command(label='Salvar', command=self.pedir_caminho_salvar)
        menubar.add_cascade(label='Arquivo', menu=menu_arquivo)
        self.janela.config(menu=menubar)

        # Callbacks a serem definidos pelo controlador
        self._on_salvar = None
        self._on_abrir = None

        menu_arquivo.entryconfig('Salvar', command=lambda: self._on_salvar and self._on_salvar())
        menu_arquivo.entryconfig('Abrir',  command=lambda: self._on_abrir  and self._on_abrir())

    def _criar_widgets(self):
        """
        @brief Cria todos os widgets da interface: labels, menus e canvas.
        """
        Label(self.janela, text='Forma').grid(row=0, column=0, padx=12, pady=6, sticky=NW)

        OptionMenu(self.janela, self.tipofigura_var,
                   'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo', 'Polígono'
                   ).grid(row=1, column=0, padx=12, sticky=NW)

        Label(self.janela, text='Borda:').grid(row=2, column=0, padx=12, pady=(12, 0), sticky=NW)
        self.btn_cor_borda = Button(self.janela, text='     ', bg=self.cor_borda,
                                    command=self.escolher_cor_borda, relief=RIDGE)
        self.btn_cor_borda.grid(row=3, column=0, padx=12, sticky=NW)

        Label(self.janela, text='Preenchimento:').grid(row=4, column=0, padx=12, pady=(12, 0), sticky=NW)
        self.btn_cor_preench = Button(self.janela, text='     ', bg=self.cor_preenchimento,
                                      command=self.escolher_cor_preenchimento, relief=RIDGE)
        self.btn_cor_preench.grid(row=5, column=0, padx=12, sticky=NW)

        self.areadesenho = Canvas(self.janela, bg='white')
        self.areadesenho.grid(row=0, column=1, rowspan=10, padx=12, pady=6, sticky=NSEW)

    def escolher_cor_borda(self):
        """
        @brief Abre o seletor de cor para a borda e atualiza o botão.
        """
        cor = colorchooser.askcolor(title='Cor da borda', color=self.cor_borda)
        if cor[1]:
            self.cor_borda = cor[1]
            self.btn_cor_borda.config(bg=self.cor_borda)

    def escolher_cor_preenchimento(self):
        """
        @brief Abre o seletor de cor para o preenchimento e atualiza o botão.
        """
        cor = colorchooser.askcolor(title='Cor de preenchimento', color=self.cor_preenchimento)
        if cor[1]:
            self.cor_preenchimento = cor[1]
            self.btn_cor_preench.config(bg=self.cor_preenchimento)

    def pedir_caminho_salvar(self):
        """
        @brief Abre o diálogo de salvar arquivo e retorna o caminho escolhido.
        @return: Caminho do arquivo ou None se cancelado.
        @rtype: str ou None
        """
        return filedialog.asksaveasfilename(
            defaultextension='.json',
            filetypes=[('Arquivo de Desenho', '*.json'), ('Todos os arquivos', '*.*')]
        )

    def pedir_caminho_abrir(self):
        """
        @brief Abre o diálogo de abrir arquivo e retorna o caminho escolhido.
        @return: Caminho do arquivo ou None se cancelado.
        @rtype: str ou None
        """
        return filedialog.askopenfilename(
            filetypes=[('Arquivo de Desenho', '*.json'), ('Todos os arquivos', '*.*')]
        )

    def desenhar_figuras(self, figuras):
        """
        @brief Limpa o canvas e redesenha todas as figuras salvas.
        @param figuras: Lista de figuras a serem desenhadas.
        @type figuras: list[Figura]
        """
        self.areadesenho.delete('all')
        for figura in figuras:
            figura.desenhar(self.areadesenho)

    def desenhar_figuranova(self, figuranova):
        """
        @brief Desenha o preview pontilhado da figura sendo criada.
        @param figuranova: Figura em construção ou None.
        @type figuranova: Figura ou None
        """
        if figuranova is not None:
            figuranova.desenhar(self.areadesenho, dash=(4, 2))
