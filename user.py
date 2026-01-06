from app.database.repositories import *

class User:
    def __init__(self, id, username, email, password, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at

        self.viagens = []


    def comprar_viagem(self, viagem_desejada):
        ...
    
    def cancelar_viagem(self,usuario,viagem_desejada):
        user = find_user_by_username(usuario)
        viagem = find_viagem_by_destination(viagem_desejada)

        delete_user_viagem(user, viagem)
    
    def tickets_viagem(self):
        return find_all_user_viagens(self.id)
    
    def login(self,username,password):
        user = find_user_by_username(username)

        if user.password != password:
            return False
        
        return True
        