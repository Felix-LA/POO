class Att05:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.normalizarTempo()

    def normalizarTempo(self):
        # Normaliza segundos -> minutos
        if self.segundos >= 60:
            self.minutos += self.segundos // 60
            self.segundos = self.segundos % 60
        
        # Normaliza minutos -> horas
        if self.minutos >= 60:
            self.horas += self.minutos // 60
            self.minutos = self.minutos % 60
        
        # Normaliza horas -> dias
        self.dias = self.horas // 24
        self.horas = self.horas % 24

    def adicionarSegundos(self, s):
        self.segundos += s
        self.normalizarTempo()

    def mostrarTempo(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d} (+{self.dias} dia(s))"

    def diferenca(self, outro_relogio):
        # Converte ambos para segundos totais
        total_self = self.horas * 3600 + self.minutos * 60 + self.segundos
        total_outro = outro_relogio.horas * 3600 + outro_relogio.minutos * 60 + outro_relogio.segundos

        # Calcula a diferença em segundos
        diferenca_seg = abs(total_self - total_outro)

        # Converte de volta para h:m:s
        horas = diferenca_seg // 3600
        diferenca_seg %= 3600
        minutos = diferenca_seg // 60
        segundos = diferenca_seg % 60

        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


# --- Exemplo de uso ---
if __name__ == "__main__":
    r1 = Att05(10, 45, 30)
    r2 = Att05(8, 15, 50)

    print("Relógio 1:", r1.mostrarTempo())
    print("Relógio 2:", r2.mostrarTempo())
    print("Diferença entre os dois:", r1.diferenca(r2))
