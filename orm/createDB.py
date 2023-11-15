from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Enum, ForeignKey

engine = create_engine('sqlite:///dataBase.db')

metadata = MetaData()

#Modelo da tabela
itens = Table('itens', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String, nullable=False),
    Column('quantidade', Integer, nullable=False),
    Column('categoria', Enum('Fones de ouvido', 'Notebook', 'CPU', 'Memória', 'SSD/HD', 'Celular', 'Película', 'Placa de video', 'Fonte'), nullable=False)
)

# Modelo da tabela de histórico
historico = Table('historico', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('item_id', Integer, ForeignKey('itens.id'), nullable=False),
    Column('acao', Enum('Editado', 'Deletado'), nullable=False), 
    Column('quantidade_ant', String),  
    Column('quantidade_atual', String)
)

metadata.create_all(engine)
