from orm import createDB
from sqlalchemy.sql import text


def add_item(nome, quantidade, categoria):
    conn = createDB.engine.connect()
    
    novo_item = text("INSERT INTO itens (nome, quantidade, categoria) VALUES (:nome, :quantidade, :categoria)")
    conn.execute(novo_item, nome=nome, quantidade=quantidade, categoria=categoria)

    conn.close()

def del_item():
    pass

def att_item():
    pass