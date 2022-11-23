from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Atores(Base):
    __tablename__ = 'atores'  # essa classe se relaciona com a tabela do banco de dados
    #  esses atributos são os atributos que vamos "puxar" do sql
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))  # isso aqui é uma chave estrangeira,
    # ele vai criar uma relação entre esse elemento e a outra tabela 'filmes', ele vai usar o 'titulo'

    def __repr__(self):
        return f'atores (nome = {self.nome}, fime = {self.titulo_filme})'
