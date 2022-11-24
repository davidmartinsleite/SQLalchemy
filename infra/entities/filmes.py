from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Filmes(Base):
    __tablename__ = 'filmes'  # essa classe se relaciona com a tabela do banco de dados
    #  esses atributos são os atributos que vamos "puxar" do sql
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Atores', backref='atores', lazy='subquery')
    # relationship('nome da tabela(classe)', 'referencia reversa')

    def __repr__(self):
        return f'Filme (titulo = {self.titulo}, ano= {self.ano})'


