from app.database.repositories import *
from app.utils import *


class Admin:
    def __init__(self):
        pass

    @staticmethod
    def adicionar_usuario(username:str,email:str,password:str):
        try:
            insert_user(username,email,password)
        except Exception as e:
            print(f"error: {e}")

    @staticmethod
    def adicionar_viagem(preco,destino,data_inicio,data_fim,horario):
        data_inicio = convert_date(data_inicio)
        data_fim = convert_date(data_fim)
        destino = convert_destination(destino)

        try:
            insert_viagem(preco, destino, data_inicio, data_fim, horario)

        except Exception as e:
            print(f"error: {e}")

    @staticmethod
    def atribuir_viagem_ao_cliente(cliente,viagem):
        cliente = find_user_by_username(cliente)
        viagem = find_viagem_by_destination(viagem.strip())

        insert_user_viagem(cliente.id,viagem.id)

