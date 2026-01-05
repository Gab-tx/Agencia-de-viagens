from queries import *
from connection import connect
from ..exception import *

def create_table():
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(CREATE_TABLE_USER)

def find(parameter:str=None):
    with connect() as CONN:
        with CONN.cursor() as cur:

            if parameter:

                try:
                    cur.execute(FIND_USER_BY_ID,(parameter,))
                    return cur.fetchone()
                except Exception:
                    pass 

                try:
                    cur.execute(FIND_USER_BY_USERNAME,(parameter,))
                    return cur.fetchone()
                except Exception:
                    pass

                try:
                    cur.execute(FIND_USER_BY_EMAIL,(parameter,))
                    return cur.fetchone()
                except Exception:
                    pass

                raise NotFindException("")
            
            try:
                cur.execute(FIND_ALL_USERS)
                return cur.fetchall()
            except Exception:
                raise NotFindException("") 
   
def find_all_user_viagens(id_user):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(FIND_ALL_USER_VIAGENS,(id_user,))
            return cur.fetchall

        
def insert_user(username:str,email:str,password:str):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(INSERT_USER,(username,email,password))

def update_user_username(username,email,password,id_user):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(UPDATE_USER_CREDENTIALS,(username,email,password,id_user))

def delete_user(id_user):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(DELETE_USER_BY_ID,(id_user,))

# --------------- user_viagem ---------------            

def insert_user_viagem(id_user,id_viagem):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(INSERT_USER_VIAGEM,(id_user,id_viagem))

def update_viagem_data(data_inicio, data_fim,id_viagem):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(UPDATE_VIAGEM_DATA,(data_inicio,data_fim,id_viagem))

def update_viagem_horario(horario,id_viagem):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(UPDATE_VIAGEM_HORARIO,(horario,id_viagem))
        
def update_viagem_preco(preco,id_viagem):
    with connect() as CONN:
        with CONN.cursor() as cur:
            cur.execute(UPDATE_VIAGEM_PRECO,(preco,id_viagem))

