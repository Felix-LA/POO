class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.data = self.dia + self.mes + self.ano
        self.anotacao = anotacao
        
        self.calendar = {}

        self.calendar[self.data] = anotacao
        print(self.calendar)

    def validar_data(self, data_atual):
        if self.data == data_atual: 
            print(f"No dia {self.dia}/{self.mes}/{self.ano} teremos: ", end='')
            return self.calendar[data_atual]           
        else: 
            return f"Nao tem nada nessa data"

    def anotar_tarefa(self, dia, mes, ano, tarefa):
        self.calendar[dia + mes + ano] = tarefa
        return f"Tarefa adicionada com sucesso!"

    def mostrar_anotacao(self):
        for j, i in enumerate(self.calendar.values()):
            print(f'({j + 1}) - {i}')



tar = Agenda('20', '04', '2025', 'jogar um fut com os cria')

print(tar.validar_data('20042025'))

print(tar.anotar_tarefa('12', '06', '2025', 'palestra do thiagao'))

tar.mostrar_anotacao()
