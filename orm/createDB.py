from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Enum

engine = create_engine('sqlite:///dataBase.db')

metadata = MetaData()

#Modelo da tabela
itens = Table('itens', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String, nullable=False),
    Column('quantidade', Integer, nullable=False),
    Column('categoria', Enum('Eletrônico', 'Decoração', 'Eletrodoméstico', ''), nullable=False)
)

metadata.create_all(engine)
