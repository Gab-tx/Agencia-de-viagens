from user import User
from viagem import Viagem
from datetime import datetime as dt

def user_to_object(fetch):
    id_user = fetch[0]
    username = fetch[1]
    email = fetch[2]
    password = fetch[3]
    timestamp = fetch[4]

    user = User(id_user,username,email,password,timestamp)
    return user

def viagem_to_object(fetch):
    id_viagem= fetch[0]
    preco = fetch[1]
    destino = fetch[2]
    data_inicio = fetch[3]
    data_fim = fetch[4]
    horario = fetch[5]

    viagem = Viagem(id_viagem,destino,preco,horario,data_inicio,data_fim)
    return viagem

def convert_date(date:str, date_format='%d/%m/%Y'):
    #Retorna uma data no padrão yyyy-mm-dd
    try:
        date_obj = dt.strptime(date.strip(), date_format)
        return date_obj.strftime('%Y-%m-%d')
    
    except ValueError as e:
        print(f'Data Inválida: {date}. Formato esperado {date_format}')

    except Exception as e:
        print(f'Error: {e}')

def convert_destination(destination:str):
    return destination.strip()
