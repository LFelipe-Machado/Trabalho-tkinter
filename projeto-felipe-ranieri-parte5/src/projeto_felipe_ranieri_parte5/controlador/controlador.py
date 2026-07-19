"""
@package controlador.controlador
@brief Módulo contendo a classe controladora do padrão MVC.
@author Felipe Machado e Ranieri Pereira
@version 3.0
@since 2026-07-19
"""

from controlador.estados import (
    EstadoLinha, EstadoRetangulo, EstadoOval,
    EstadoCirculo, EstadoRabisco, EstadoPoligono
)


class Controlador:
    """
    @brief Classe responsável por conectar a Visão ao Modelo no padrão MVC.

    Gerencia os eventos do mouse delegando-os ao estado (padrão State)
    correspondente à ferramenta atualmente selecionada na Visão, e
    coordena as operações de salvar e abrir desenhos.

    Antes da Etapa 5, este método consultava `tipofigura_var` e decidia
    o que fazer através de uma cadeia de if/elif em cada evento. Agora
    essa responsabilidade pertence às classes de controlador.estados:
    o Controlador apenas identifica o estado atual e delega o evento a
    ele, sem precisar conhecer o comportamento de cada figura.

    @author Felipe Machado e Ranieri Pereira
    @version 3.0
    @since 2026-07-19
    """

    def __init__(self, visao, desenho):
        """
        @brief Inicializa o controlador conectando visão, modelo e estados.
        @param visao: Instância da Visão com os widgets tkinter.
        @type visao: visao.visao.Visao
        @param desenho: Instância do Desenho com a lista de figuras.
        @type desenho: modelo.figuras.Desenho
        """
        self.visao = visao
        self.desenho = desenho
        self.figuranova = None

        self.estados = {
            'Linha':     EstadoLinha(),
            'Retângulo': EstadoRetangulo(),
            'Oval':      EstadoOval(),
            'Círculo':   EstadoCirculo(),
            'Rabisco':   EstadoRabisco(),
            'Polígono':  EstadoPoligono(),
        }

        self.visao.areadesenho.bind('<ButtonPress-1>',   self.iniciar_figuranova)
        self.visao.areadesenho.bind('<B1-Motion>',       self.atualizar_figuranova)
        self.visao.areadesenho.bind('<ButtonRelease-1>', self.incluir_figuranova)
        self.visao.areadesenho.bind('<ButtonPress-3>',   self.finalizar_poligono)

        self.visao._on_salvar = self.salvar
        self.visao._on_abrir  = self.abrir

    def _estado_atual(self):
        """
        @brief Obtém o estado correspondente à ferramenta selecionada na Visão.
        @return: Instância de EstadoDesenho associada ao tipo de figura atual.
        @rtype: controlador.estados.EstadoDesenho
        """
        tipo = self.visao.tipofigura_var.get()
        return self.estados[tipo]

    def iniciar_figuranova(self, event):
        """
        @brief Delega o clique do botão esquerdo do mouse ao estado atual.

        Se já existe um polígono em construção, o próprio EstadoPoligono
        decide adicionar um novo ponto a ele em vez de criar outra figura.

        @param event: Evento de mouse com coordenadas x e y.
        @type event: tkinter.Event
        """
        self._estado_atual().iniciar(self, event)

    def atualizar_figuranova(self, event):
        """
        @brief Delega o arraste do mouse ao estado atual.
        @param event: Evento de mouse com coordenadas x e y.
        @type event: tkinter.Event
        """
        self._estado_atual().atualizar(self, event)

    def incluir_figuranova(self, event):
        """
        @brief Delega o soltar do botão esquerdo do mouse ao estado atual.

        Polígono não é finalizado aqui — requer clique direito.

        @param event: Evento de mouse.
        @type event: tkinter.Event
        """
        self._estado_atual().incluir(self, event)

    def finalizar_poligono(self, event):
        """
        @brief Delega o clique com o botão direito do mouse ao estado atual.
        @param event: Evento de mouse.
        @type event: tkinter.Event
        """
        self._estado_atual().finalizar_poligono(self, event)

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
