import pandas as pd
import math

class MetodoFalsaPosicao:
    def __init__(self, a, b, digitos, erro):
        self.a = a
        self.b = b
        self.digitos = digitos
        self.erro = erro

    def funcao(self, x):
        return math.pow(x, 3) + x + 1

    def truncamento(self, valor):
        negativo = valor < 0
        valor = abs(valor)
        if len(str(valor)) > self.digitos:
            valor_str = str(valor)
            valor_leitura = valor_str[:self.digitos + 1]
            apos_truncamento = valor_str[:self.digitos + 2]
            if int(valor_leitura[-1]) % 2 != 0:
                if int(apos_truncamento[-1]) in [0, 1, 2, 3, 4]:
                    resultado = float(valor_leitura)
                elif int(apos_truncamento[-1]) in [5, 6, 7, 8, 9]:
                    valor_adicional = str(int(valor_leitura[-1]) + 1)
                    valor_leitura = valor_leitura[:self.digitos] + valor_adicional
                    resultado = float(valor_leitura)
            else:
                resultado = float(valor_leitura)
        else:
            resultado = valor
        return -resultado if negativo else resultado

    def calcular(self):
        a = self.a
        b = self.b
        erro = self.erro
        d = self.digitos

        interacao = 1
        fa = self.truncamento(self.funcao(a))
        fb = self.truncamento(self.funcao(b))
        xo = self.truncamento(((a * fb) - (b * fa)) / (fb - fa))
        modulo_f_xo = abs(self.truncamento(self.funcao(xo)))

        a_lista = []
        b_lista = []
        xo_lista = []
        f_xo_lista = []
        b_menos_a_lista = []
        modulo_f_xo_lista = []
        fa_lista = []
        fb_lista = []
        interacao_lista = []

        while modulo_f_xo > erro:
            interacao_lista.append(interacao)
            a_lista.append(a)
            b_lista.append(b)

            fa = self.truncamento(self.funcao(a))
            fb = self.truncamento(self.funcao(b))
            fa_lista.append(fa)
            fb_lista.append(fb)

            xo = self.truncamento(((a * fb) - (b * fa)) / (fb - fa))
            xo_lista.append(xo)

            f_xo = self.truncamento(self.funcao(xo))
            f_xo_lista.append(f_xo)

            b_menos_a = abs(self.truncamento(b - a))
            b_menos_a_lista.append(b_menos_a)

            modulo_f_xo = abs(f_xo)
            modulo_f_xo_lista.append(modulo_f_xo)

            if fa * f_xo < 0:
                b = xo
            else:
                a = xo

            interacao += 1

        df = pd.DataFrame({
            'Interação': interacao_lista,
            'a': a_lista,
            'b': b_lista,
            'x0': xo_lista,
            'f(a)': fa_lista,
            'f(b)': fb_lista,
            'f(x0)': f_xo_lista,
            '|b - a|': b_menos_a_lista,
            '|f(x0)|': modulo_f_xo_lista
        })

        print(df)
        print(f"\nRaiz é aproximadamente: {xo}")

metodo = MetodoFalsaPosicao(a=-2, b=0, digitos=5, erro=0.1)
metodo.calcular()
