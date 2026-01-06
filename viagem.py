from app.database.repositories import *

class Viagem:
    def __init__(self,id_viagem,destino,preco,horario,data_inicio, data_fim):
        self.id = id_viagem
        self.destino = destino
        self._preco = preco
        self._horario = horario
        self._data = f"{data_inicio} - {data_fim}"

    @property
    def data(self):
        return self.data
    
    @data.setter
    # Anotações - Se isso fosse realmente uma aplicação de viagens seria importante avisar a mudança de data e motivo 
    # juntamente com a opção de reembolso/cancelamento
    def data(self, nova_data_inicio, nova_data_fim):

        self.data = f"{nova_data_inicio} - {nova_data_fim}"
        self.data_inicio = nova_data_inicio
        self.data_fim = nova_data_fim

        update_viagem_data(nova_data_inicio, nova_data_fim, self.id_viagem)

    @property
    def horario(self):
        return self.horario
    @horario.setter
    def horario(self, novo_horario):
        self.horario = novo_horario

        update_viagem_horario(novo_horario,self.id_viagem)

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self,novo_preco):
        self._preco = novo_preco

        update_viagem_preco(novo_preco,self.id_viagem)

    def cancelar_viagem():
        ...
        