CREATE_TABLE_USER = """CREATE TABLE IF EXISTS tbl_user(
id_user SERIAL PRIMARY KEY,
username VARCHAR(20) NOT NULL,
email VARCHAR(50) NOT NULL,
password VARCHAR(20) NOT NULL,
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);"""


CREATE_TABLE_USER_VIAGEM = """CREATE TABLE IF EXISTS tbl_user_viagem(
id_usuario INT,
id_viagem INT,
created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

FOREING KEY (id_usuario) REFERENCES tbl_user(id_usuario) ON DELETE CASCADE
FOREING KEY (id_viagem) REFERENCES tbl_viagens(id_viagem) ON DELETE CASCADE
):"""

INSERT_USER_VIAGEM = """INSERT INTO tbl_user_viagem(id_usuario,id_viagem)
VALUES(%s,%s)"""

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

CREATE_TABLE_VIAGENS = """CREATE TABLE tbl_viagens (
    id_viagem INT PRIMARY KEY AUTO_INCREMENT,
    preco FLOAT NOT NULL,
    destino VARCHAR(100) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    horario VARCHAR(10) NOT NULL
);"""

FIND_VIAGENS_BY_USER = """SELECT * FROM tbl_user_viagem WHERE id_usuario = %s"""

UPDATE_VIAGEM_DATA = """UPDATE tbl_viagens
SET data_inicio = %s, data_fim = %s
WHERE id_viagem = %s"""

UPDATE_VIAGEM_PRECO ="""UPDATE tbl_viagens
SET preco = %s
WHERE id_viagem = %s"""

UPDATE_VIAGEM_HORARIO ="""UPDATE tbl_viagens
SET horario = %s
WHERE id_viagem = %s"""


