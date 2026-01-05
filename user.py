from app.database.repositories import *

class User:
    def __init__(self, id, username, email, password, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at

        self.viagens = {find_all_user_viagens(self.id)}


    def comprar_viagem(self, viagem_desejada):
        # if ...

        # self.viagens.append(viagem_desejada)
        ...
    
    def cancelar_viagem():
        ...
    
    def tickets_viagem(self) -> list:
        return self.viagens
    
    def login(self):
        ...
        