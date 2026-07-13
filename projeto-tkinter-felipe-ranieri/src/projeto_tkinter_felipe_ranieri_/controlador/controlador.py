"""
@package controlador.controlador
@brief Módulo contendo a classe controladora do padrão MVC.
@author Felipe Machado e Ranieri Pereira
@version 2.0
@since 2026-07-08
"""

from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono


class Controlador:
    """
    @brief Classe responsável por conectar a Visão ao Modelo no padrão MVC.

    Gerencia os eventos do mouse, cria as figuras corretas e coordena
    as operações de salvar e abrir desenhos.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-08
    """

    def __init__(self, visao, desenho):
        """
        @brief Inicializa o controlador conectando visão e modelo.
        @param visao: Instância da Visão com os widgets tkinter.
        @type visao: visao.visao.Visao
        @param desenho: Instância do Desenho com a lista de figuras.
        @type desenho: modelo.figuras.Desenho
        """
        self.visao = visao
        self.desenho = desenho
        self.figuranova = None

        self.visao.areadesenho.bind('<ButtonPress-1>',   self.iniciar_figuranova)
        self.visao.areadesenho.bind('<B1-Motion>',       self.atualizar_figuranova)
        self.visao.areadesenho.bind('<ButtonRelease-1>', self.incluir_figuranova)
        self.visao.areadesenho.bind('<ButtonPress-3>',   self.finalizar_poligono)

        self.visao._on_salvar = self.salvar
        self.visao._on_abrir  = self.abrir

    def iniciar_figuranova(self, event):
        """
        @brief Cria uma nova figura ao pressionar o botão do mouse.

        Se já existe um polígono em construção, adiciona um ponto a ele.

        @param event: Evento de mouse com coordenadas x e y.
        @type event: tkinter.Event
        """
        tipo = self.visao.tipofigura_var.get()
        cb   = self.visao.cor_borda
        cp   = self.visao.cor_preenchimento

        if tipo == 'Polígono' and self.figuranova is not None:
            self.figuranova.adicionar_ponto(event.x, event.y)
            self.visao.desenhar_figuras(self.desenho.figuras)
            self.visao.desenhar_figuranova(self.figuranova)
            return

        if tipo == 'Linha':
            self.figuranova = Linha(event.x, event.y, cb)
        elif tipo == 'Rabisco':
            self.figuranova = Rabisco(event.x, event.y, cb)
        elif tipo == 'Retângulo':
            self.figuranova = Retangulo(event.x, event.y, cb, cp)
        elif tipo == 'Oval':
            self.figuranova = Oval(event.x, event.y, cb, cp)
        elif tipo == 'Círculo':
            self.figuranova = Circulo(event.x, event.y, cb, cp)
        elif tipo == 'Polígono':
            self.figuranova = Poligono(event.x, event.y, cb, cp)

    def atualizar_figuranova(self, event):
        """
        @brief Atualiza a figura em construção enquanto o mouse é arrastado.
        @param event: Evento de mouse com coordenadas x e y.
        @type event: tkinter.Event
        """
        if self.figuranova is None:
            return

        tipo = self.visao.tipofigura_var.get()

        if tipo == 'Rabisco':
            self.figuranova.adicionar_ponto(event.x, event.y)
        elif tipo == 'Polígono':
            self.visao.desenhar_figuras(self.desenho.figuras)
            self.visao.desenhar_figuranova(self.figuranova)
            ultimo = self.figuranova.pontos[-1]
            self.visao.areadesenho.create_line(ultimo[0], ultimo[1], event.x, event.y,
                                               fill=self.figuranova.cor_borda, dash=(4, 2))
            return
        else:
            self.figuranova.atualizar(event.x, event.y)

        self.visao.desenhar_figuras(self.desenho.figuras)
        self.visao.desenhar_figuranova(self.figuranova)

    def incluir_figuranova(self, event):
        """
        @brief Finaliza e salva a figura ao soltar o botão do mouse.

        Polígono não é finalizado aqui — requer clique direito.

        @param event: Evento de mouse.
        @type event: tkinter.Event
        """
        if self.visao.tipofigura_var.get() == 'Polígono':
            return
        if self.figuranova is not None and not self.figuranova.incompleta():
            self.desenho.figuras.append(self.figuranova)
            self.figuranova = None
        self.visao.desenhar_figuras(self.desenho.figuras)

    def finalizar_poligono(self, event):
        """
        @brief Finaliza o polígono ao clicar com o botão direito do mouse.
        @param event: Evento de mouse.
        @type event: tkinter.Event
        """
        if self.figuranova is not None and not self.figuranova.incompleta():
            self.desenho.figuras.append(self.figuranova)
            self.figuranova = None
        self.visao.desenhar_figuras(self.desenho.figuras)

    def salvar(self):
        """
        @brief Abre o diálogo de salvar e persiste o desenho em JSON.
        """
        caminho = self.visao.pedir_caminho_salvar()
        if caminho:
            self.desenho.salvar(caminho)

    def abrir(self):
        """
        @brief Abre o diálogo de abrir e carrega um desenho salvo em JSON.
        """
        caminho = self.visao.pedir_caminho_abrir()
        if caminho:
            self.desenho.abrir(caminho)
            self.visao.desenhar_figuras(self.desenho.figuras)

