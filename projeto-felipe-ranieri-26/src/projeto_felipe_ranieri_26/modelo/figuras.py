class Figura:
    def __init__(self, cor_borda='black', cor_preenchimento=''):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    def desenhar(self, canvas, dash=()):
        pass
    def incompleta(self):
        pass

class FiguraDeArrastar(Figura):
    def __init__(self, x0, y0, cor_borda='black', cor_preenchimento=''):
        super().__init__(cor_borda, cor_preenchimento)
        self.x0 = x0; self.y0 = y0; self.x1 = x0; self.y1 = y0
    def atualizar(self, x1, y1):
        self.x1 = x1; self.y1 = y1
    def incompleta(self):
        return (self.x0, self.y0) == (self.x1, self.y1)

class Linha(FiguraDeArrastar):
    def __init__(self, x0, y0, cor_borda='black'):
        super().__init__(x0, y0, cor_borda=cor_borda)
    def desenhar(self, canvas, dash=()):
        canvas.create_line(self.x0, self.y0, self.x1, self.y1, fill=self.cor_borda, dash=dash)

class Retangulo(FiguraDeArrastar):
    def desenhar(self, canvas, dash=()):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

class Oval(FiguraDeArrastar):
    def desenhar(self, canvas, dash=()):
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

class Circulo(FiguraDeArrastar):
    def atualizar(self, x1, y1):
        lado = min(abs(x1 - self.x0), abs(y1 - self.y0))
        self.x1 = self.x0 + (lado if x1 >= self.x0 else -lado)
        self.y1 = self.y0 + (lado if y1 >= self.y0 else -lado)
    def desenhar(self, canvas, dash=()):
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

class Rabisco(Figura):
    def __init__(self, x, y, cor_borda='black'):
        super().__init__(cor_borda=cor_borda)
        self.pontos = [(x, y)]
    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))
    def desenhar(self, canvas, dash=()):
        if len(self.pontos) >= 2:
            canvas.create_line(self.pontos, fill=self.cor_borda, smooth=True, dash=dash)
    def incompleta(self):
        return len(self.pontos) <= 1

class Poligono(Figura):
    def __init__(self, x, y, cor_borda='black', cor_preenchimento=''):
        super().__init__(cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.pontos = [(x, y)]
    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))
    def desenhar(self, canvas, dash=()):
        if len(self.pontos) >= 3:
            canvas.create_polygon(self.pontos, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)
        elif len(self.pontos) == 2:
            canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)
    def incompleta(self):
        return len(self.pontos) < 3

class Desenho:
    def __init__(self):
        self.figuras = []
