"""
@package modelo.figuras
@brief Módulo com a hierarquia de classes para figuras geométricas e o modelo do desenho.
@author Felipe Machado e Ranieri Pereira
@version 2.0
@since 2026-07-01
"""

import json


class Figura:
    """
    @brief Classe base para todas as figuras geométricas do sistema.

    Define a interface comum (desenhar, incompleta, to_dict) que
    todas as subclasses devem implementar.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self, cor_borda='black', cor_preenchimento=''):
        """
        @brief Inicializa a figura com cores de borda e preenchimento.
        @param cor_borda: Cor da borda em hex ou nome CSS. Default: 'black'.
        @type cor_borda: str
        @param cor_preenchimento: Cor de preenchimento em hex ou nome CSS. Default: vazio.
        @type cor_preenchimento: str
        """
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha a figura no canvas tkinter.
        @param canvas: Canvas tkinter onde a figura será desenhada.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço. Tupla vazia para linha sólida.
        @type dash: tuple
        """
        pass

    def incompleta(self):
        """
        @brief Verifica se a figura tem tamanho válido para ser salva.
        @return: True se a figura não possui tamanho válido.
        @rtype: bool
        """
        pass

    def to_dict(self):
        """
        @brief Serializa a figura para um dicionário.
        @return: Dicionário com tipo e cores da figura.
        @rtype: dict
        """
        return {
            'tipo': self.__class__.__name__,
            'cor_borda': self.cor_borda,
            'cor_preenchimento': self.cor_preenchimento
        }


class FiguraDeArrastar(Figura):
    """
    @brief Classe intermediária para figuras definidas por dois pontos (início e fim do arraste).

    Subclasses: Linha, Retangulo, Oval, Circulo.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self, x0, y0, cor_borda='black', cor_preenchimento=''):
        """
        @brief Inicializa a figura com o ponto inicial do arraste.
        @param x0: Coordenada X do ponto inicial.
        @type x0: int
        @param y0: Coordenada Y do ponto inicial.
        @type y0: int
        @param cor_borda: Cor da borda.
        @type cor_borda: str
        @param cor_preenchimento: Cor de preenchimento.
        @type cor_preenchimento: str
        """
        super().__init__(cor_borda, cor_preenchimento)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0
        self.y1 = y0

    def atualizar(self, x1, y1):
        """
        @brief Atualiza o ponto final durante o arraste do mouse.
        @param x1: Nova coordenada X do ponto final.
        @type x1: int
        @param y1: Nova coordenada Y do ponto final.
        @type y1: int
        """
        self.x1 = x1
        self.y1 = y1

    def incompleta(self):
        """
        @brief Verifica se ponto inicial e final são iguais.
        @return: True se a figura não possui área.
        @rtype: bool
        """
        return (self.x0, self.y0) == (self.x1, self.y1)

    def to_dict(self):
        """
        @brief Serializa os atributos da figura de arrastar.
        @return: Dicionário com tipo, coordenadas e cores.
        @rtype: dict
        """
        d = super().to_dict()
        d.update({'x0': self.x0, 'y0': self.y0, 'x1': self.x1, 'y1': self.y1})
        return d


class Linha(FiguraDeArrastar):
    """
    @brief Representa uma linha reta entre dois pontos.
    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self, x0, y0, cor_borda='black'):
        """
        @brief Inicializa a linha com ponto inicial e cor.
        @param x0: Coordenada X do ponto inicial.
        @type x0: int
        @param y0: Coordenada Y do ponto inicial.
        @type y0: int
        @param cor_borda: Cor da linha.
        @type cor_borda: str
        """
        super().__init__(x0, y0, cor_borda=cor_borda)

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha a linha no canvas.
        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço.
        @type dash: tuple
        """
        canvas.create_line(self.x0, self.y0, self.x1, self.y1,
                           fill=self.cor_borda, dash=dash)


class Retangulo(FiguraDeArrastar):
    """
    @brief Representa um retângulo com borda e preenchimento.
    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha o retângulo no canvas.
        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço para a borda.
        @type dash: tuple
        """
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1,
                                outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)


class Oval(FiguraDeArrastar):
    """
    @brief Representa uma oval (elipse) com borda e preenchimento.
    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha a oval no canvas.
        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço para a borda.
        @type dash: tuple
        """
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1,
                           outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)


class Circulo(FiguraDeArrastar):
    """
    @brief Representa um círculo com proporção forçada 1:1.

    Sobrescreve atualizar para garantir que largura e altura sejam iguais.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def atualizar(self, x1, y1):
        """
        @brief Atualiza o ponto final garantindo proporção quadrada.
        @param x1: Coordenada X atual do mouse.
        @type x1: int
        @param y1: Coordenada Y atual do mouse.
        @type y1: int
        """
        lado = min(abs(x1 - self.x0), abs(y1 - self.y0))
        self.x1 = self.x0 + (lado if x1 >= self.x0 else -lado)
        self.y1 = self.y0 + (lado if y1 >= self.y0 else -lado)

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha o círculo no canvas.
        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço para a borda.
        @type dash: tuple
        """
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1,
                           outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)


class Rabisco(Figura):
    """
    @brief Representa um traço livre desenhado com o mouse.

    Acumula pontos conforme o mouse é arrastado, criando uma linha suave.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self, x, y, cor_borda='black'):
        """
        @brief Inicializa o rabisco com o ponto inicial.
        @param x: Coordenada X do ponto inicial.
        @type x: int
        @param y: Coordenada Y do ponto inicial.
        @type y: int
        @param cor_borda: Cor do traço.
        @type cor_borda: str
        """
        super().__init__(cor_borda=cor_borda)
        self.pontos = [(x, y)]

    def adicionar_ponto(self, x, y):
        """
        @brief Adiciona um novo ponto ao traço.
        @param x: Coordenada X do novo ponto.
        @type x: int
        @param y: Coordenada Y do novo ponto.
        @type y: int
        """
        self.pontos.append((x, y))

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha o traço livre no canvas.
        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço.
        @type dash: tuple
        """
        if len(self.pontos) >= 2:
            canvas.create_line(self.pontos, fill=self.cor_borda, smooth=True, dash=dash)

    def incompleta(self):
        """
        @brief Verifica se o rabisco possui pontos suficientes.
        @return: True se tiver apenas um ponto.
        @rtype: bool
        """
        return len(self.pontos) <= 1

    def to_dict(self):
        """
        @brief Serializa o rabisco para um dicionário.
        @return: Dicionário com tipo, pontos e cor.
        @rtype: dict
        """
        d = super().to_dict()
        d['pontos'] = self.pontos
        return d


class Poligono(Figura):
    """
    @brief Representa um polígono definido por múltiplos cliques do mouse.

    O usuário clica para adicionar vértices e finaliza com o botão direito.
    Requer pelo menos 3 pontos para ser considerado completo.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self, x, y, cor_borda='black', cor_preenchimento=''):
        """
        @brief Inicializa o polígono com o primeiro vértice.
        @param x: Coordenada X do primeiro vértice.
        @type x: int
        @param y: Coordenada Y do primeiro vértice.
        @type y: int
        @param cor_borda: Cor da borda.
        @type cor_borda: str
        @param cor_preenchimento: Cor de preenchimento.
        @type cor_preenchimento: str
        """
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.pontos = [(x, y)]

    def adicionar_ponto(self, x, y):
        """
        @brief Adiciona um novo vértice ao polígono.
        @param x: Coordenada X do novo vértice.
        @type x: int
        @param y: Coordenada Y do novo vértice.
        @type y: int
        """
        self.pontos.append((x, y))

    def desenhar(self, canvas, dash=()):
        """
        @brief Desenha o polígono no canvas.

        Com 3 ou mais pontos desenha o polígono fechado.
        Com 2 pontos desenha apenas uma linha de preview.

        @param canvas: Canvas tkinter.
        @type canvas: tkinter.Canvas
        @param dash: Padrão de traço para a borda.
        @type dash: tuple
        """
        if len(self.pontos) >= 3:
            canvas.create_polygon(self.pontos, outline=self.cor_borda,
                                  fill=self.cor_preenchimento, dash=dash)
        elif len(self.pontos) == 2:
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)

    def incompleta(self):
        """
        @brief Verifica se o polígono possui vértices suficientes.
        @return: True se tiver menos de 3 vértices.
        @rtype: bool
        """
        return len(self.pontos) < 3

    def to_dict(self):
        """
        @brief Serializa o polígono para um dicionário.
        @return: Dicionário com tipo, pontos e cores.
        @rtype: dict
        """
        d = super().to_dict()
        d['pontos'] = self.pontos
        return d


def figura_from_dict(d):
    """
    @brief Reconstrói uma figura a partir de um dicionário serializado.
    @param d: Dicionário com os dados da figura incluindo o campo 'tipo'.
    @type d: dict
    @return: Instância da subclasse de Figura correspondente.
    @rtype: Figura
    """
    tipo = d['tipo']
    cb = d['cor_borda']
    cp = d.get('cor_preenchimento', '')

    if tipo == 'Linha':
        f = Linha(d['x0'], d['y0'], cb)
        f.x1 = d['x1']
        f.y1 = d['y1']
    elif tipo == 'Retangulo':
        f = Retangulo(d['x0'], d['y0'], cb, cp)
        f.x1 = d['x1']
        f.y1 = d['y1']
    elif tipo == 'Oval':
        f = Oval(d['x0'], d['y0'], cb, cp)
        f.x1 = d['x1']
        f.y1 = d['y1']
    elif tipo == 'Circulo':
        f = Circulo(d['x0'], d['y0'], cb, cp)
        f.x1 = d['x1']
        f.y1 = d['y1']
    elif tipo == 'Rabisco':
        f = Rabisco(0, 0, cb)
        f.pontos = [tuple(p) for p in d['pontos']]
    elif tipo == 'Poligono':
        f = Poligono(0, 0, cb, cp)
        f.pontos = [tuple(p) for p in d['pontos']]
    return f


class Desenho:
    """
    @brief Representa o desenho completo, contendo todas as figuras.

    Gerencia a coleção de figuras e implementa persistência via JSON.

    @author Felipe Machado e Ranieri Pereira
    @version 2.0
    @since 2026-07-01
    """

    def __init__(self):
        """
        @brief Inicializa um desenho vazio.
        """
        self.figuras = []

    def salvar(self, caminho):
        """
        @brief Salva o desenho em um arquivo JSON.
        @param caminho: Caminho completo do arquivo de destino.
        @type caminho: str
        @raises IOError: Se houver erro ao escrever o arquivo.
        """
        dados = [fig.to_dict() for fig in self.figuras]
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def abrir(self, caminho):
        """
        @brief Carrega um desenho a partir de um arquivo JSON.

        Substitui as figuras atuais pelas carregadas do arquivo.

        @param caminho: Caminho completo do arquivo a ser aberto.
        @type caminho: str
        @raises IOError: Se houver erro ao ler o arquivo.
        """
        with open(caminho, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        self.figuras = [figura_from_dict(d) for d in dados]
