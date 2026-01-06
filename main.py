from app.database.repositories import *
from user import *
from viagem import *
from admin import *

def main():
    create_table_user()
    create_table_viagem()
    create_table_user_viagem()

    Admin.adicionar_usuario("jeremi", "jeremias@gmail.com","jerejere")
    Admin.adicionar_viagem(1099.0, "Rio de Janeiro","10/02/2026","10/03/2026","17h")
    Admin.atribuir_viagem_ao_cliente("jeremi","Rio de Janeiro")
    


if __name__ == "__main__":
    main()