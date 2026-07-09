from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo, Poligono

class Controlador:
    def __init__(self, visao, desenho):
        self.visao = visao
        self.desenho = desenho
        self.figuranova = None
        self.visao.areadesenho.bind('<ButtonPress-1>',   self.iniciar_figuranova)
        self.visao.areadesenho.bind('<B1-Motion>',       self.atualizar_figuranova)
        self.visao.areadesenho.bind('<ButtonRelease-1>', self.incluir_figuranova)
        self.visao.areadesenho.bind('<ButtonPress-3>',   self.finalizar_poligono)

    def iniciar_figuranova(self, event):
        tipo = self.visao.tipofigura_var.get()
        cb = self.visao.cor_borda
        cp = self.visao.cor_preenchimento
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
        if self.visao.tipofigura_var.get() == 'Polígono':
            return
        if self.figuranova is not None and not self.figuranova.incompleta():
            self.desenho.figuras.append(self.figuranova)
            self.figuranova = None
        self.visao.desenhar_figuras(self.desenho.figuras)

    def finalizar_poligono(self, event):
        if self.figuranova is not None and not self.figuranova.incompleta():
            self.desenho.figuras.append(self.figuranova)
            self.figuranova = None
        self.visao.desenhar_figuras(self.desenho.figuras)
