CREATE_TABLE_USER = """CREATE TABLE IF NOT EXISTS tbl_user(
id_user SERIAL PRIMARY KEY,
username VARCHAR(20) UNIQUE NOT NULL,
email VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(20) UNIQUE NOT NULL,
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);"""


INSERT_USER = """INSERT INTO tbl_user(username,email,password)
VALUES (%s,%s,%s)"""

UPDATE_USER_CREDENTIALS = """UPDATE tbl_user
SET name = %s, email = %s, password = %s
WHERE id_user = %s"""

FIND_ALL_USERS = """SELECT * FROM tbl_user"""

FIND_USER_BY_ID = """SELECT * FROM tbl_user WHERE id_user = %s"""

FIND_USER_BY_USERNAME = """SELECT * FROM tbl_user WHERE username = %s"""

FIND_USER_BY_EMAIL ="""SELECT * FROM tbl_user WHERE email = %s"""

FIND_ALL_USER_VIAGENS = """SELECT * FROM tbl_viagens
INNER JOIN tbl_user_viagem 
ON tbl_viagens.id_viagem = tbl_user_viagem.id_viagem
WHERE tbl_user_viagem.id_user = %s"""

DELETE_USER_BY_ID = """DELETE FROM tbl_user WHERE id_user = %s"""

# ------------- crud viagens ------------------

CREATE_TABLE_VIAGENS = """CREATE TABLE IF NOT EXISTS tbl_viagens (
    id_viagem SERIAL PRIMARY KEY,
    preco FLOAT NOT NULL,
    destino VARCHAR(100) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    horario VARCHAR(10) NOT NULL
);"""

INSERT_VIAGEM = """INSERT INTO tbl_viagens(preco,destino,data_inicio,data_fim, horario)
VALUES(%s,%s,%s,%s,%s)"""

FIND_VIAGENS_BY_USER = """SELECT * FROM tbl_user_viagem WHERE id_usuario = %s"""

FIND_VIAGEM_BY_DESTINATION = """SELECT * FROM tbl_viagens WHERE destino = %s""" 

UPDATE_VIAGEM_DATA = """UPDATE tbl_viagens
SET data_inicio = %s, data_fim = %s
WHERE id_viagem = %s"""

UPDATE_VIAGEM_PRECO ="""UPDATE tbl_viagens
SET preco = %s
WHERE id_viagem = %s"""

UPDATE_VIAGEM_HORARIO ="""UPDATE tbl_viagens
SET horario = %s
WHERE id_viagem = %s"""

# ----------- Relação user_viagem --------------

CREATE_TABLE_USER_VIAGEM = """CREATE TABLE IF NOT EXISTS tbl_user_viagem(
id_usuario INT UNIQUE,
id_viagem INT UNIQUE,
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (id_usuario) REFERENCES tbl_user(id_user) ON DELETE CASCADE,
FOREIGN KEY (id_viagem) REFERENCES tbl_viagens(id_viagem) ON DELETE CASCADE
);"""

INSERT_USER_VIAGEM = """INSERT INTO tbl_user_viagem(id_usuario,id_viagem)
VALUES(%s,%s)"""

DELETE_USER_VIAGEM = """DELETE FROM tbl_user_viagem WHERE id_usuario = %s AND id_viagem = %s"""


