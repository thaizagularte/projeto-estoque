from orm import createDB
from sqlalchemy.sql import text


def add_item(nome, quantidade, categoria):
    conn = createDB.engine.connect()
    
    novo_item = text("INSERT INTO itens (nome, quantidade, categoria) VALUES (:nome, :quantidade, :categoria)")
    conn.execute(novo_item, nome=nome, quantidade=quantidade, categoria=categoria)

    conn.close()

def del_item(item_id):
    conn = createDB.engine.connect()
    
    quantidade = conn.execute(text("SELECT quantidade FROM itens WHERE id = :item_id"))
    
    att_historico = text("INSERT INTO historico (item_id, acao, quantidade_ant, quantidade_att) VALUES (:item_id, :acao, : quantidade_ant, :quantidade_att)")
    conn.execute(att_historico, item_id=item_id, acao="Deletado", quantidade_ant= quantidade, quantidade_att=quantidade)

    delete_item = text("DELETE FROM itens WHERE id = :item_id")
    conn.execute(delete_item, item_id=item_id)

    conn.close()

def max_quantidade(item_id):
    conn = createDB.engine.connect()

    quant_atual = conn.execute(text("SELECT quantidade FROM itens WHERE id = :item_id"), item_id=item_id).scalar()
    quant_att = quant_atual + 1
    conn.execute(text("UPDATE itens SET quantidade = :quant_att WHERE id = :item_id"), quant_att=quant_att, item_id=item_id)
    
    att_historico = text("INSERT INTO historico (item_id, acao, quantidade_ant, quantidade_att) VALUES (:item_id, :acao, : quantidade_ant, :quantidade_att)")
    conn.execute(att_historico, item_id=item_id, acao="Editado", quantidade_ant= quant_atual, quantidade_att=quant_att)

    conn.close()


def min_quantidade(item_id):
    conn = createDB.engine.connect()

    quant_atual = conn.execute(text("SELECT quantidade FROM itens WHERE id = :item_id"), item_id=item_id).scalar()
    quant_att = quant_atual - 1
    conn.execute(text("UPDATE itens SET quantidade = :quant_att WHERE id = :item_id"), quant_att=quant_att, item_id=item_id)
    
    att_historico = text("INSERT INTO historico (item_id, acao, quantidade_ant, quantidade_att) VALUES (:item_id, :acao, : quantidade_ant, :quantidade_att)")
    conn.execute(att_historico, item_id=item_id, acao="Editado", quantidade_ant= quant_atual, quantidade_att=quant_att)

    conn.close()
 

def att_item(item_id, novo_nome,nova_quantidade, nova_categoria):
    conn = createDB.engine.connect()

    update_item = text("UPDATE itens SET nome = :novo_nome, quantidade = :nova_quantidade, categoria = :nova_categoria WHERE id = :item_id")
    conn.execute(update_item, item_id=item_id, novo_nome=novo_nome, nova_quantidade=nova_quantidade, nova_categoria=nova_categoria)

    conn.close()

def relatorio():
    conn = createDB.engine.connect()

    editado = text("SELECT acao FROM historico WHERE acao = 'Editado' ")
    deletado = text("SELECT acao FROM historico WHERE acao = 'Deletado' ")

    resultado_editado = conn.execute(editado).fetchall()
    resultado_deletado = conn.execute(deletado).fetchall()

    conn.close()

    return resultado_editado, resultado_deletado





