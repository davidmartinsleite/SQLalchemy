from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# conifigurações
engine = create_engine("mysql+pymysql://root:@localhost:3306/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)  # vamos criar uma seção e a mesma será vinculada na "engine"
                                     # então vamos criar uma sessão baseada nas conexões do banco de dados
session = Session()  # tambem vamos criar uma cessão básica

# entidades
class Filmes(Base):
    __tablename__ = 'filmes'  # essa classe se relaciona com a tabela do banco de dados
    #  esses atributos são os atributos que vamos "puxar" do sql
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship('Atores', backref='atores')

    def __repr__(self):  # fazer uma representação disso...mostrar de uma forma mais amigavel
        return f'Filme (titulo= {self.titulo}, ano={self.ano}, atores = {[ator.nome for ator in self.atores]})'


class Atores(Base):
    __tablename__ = 'atores'  # essa classe se relaciona com a tabela do banco de dados
    #  esses atributos são os atributos que vamos "puxar" do sql
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo'))  # isso aqui é uma chave estrangeira,
    # ele vai criar uma relação entre esse elemento e a outra tabela 'filmes', ele vai usar o 'titulo'

    def __repr__(self):
        return f'atores (nome = {self.nome}, fime = {self.titulo_filme})'


# SQL
#Insert
data_isert = Filmes(titulo='batman', genero='acao', ano=1991)  # criamos uma instacia da classe
session.add(data_isert)  # primeiro vou adicionar a lista de itens a serem enviados
session.commit()  # depois que fazemos algum processo temos que fazer o "commit" para enviar ao banco de dados


#Delete
session.query(Filmes).filter(Filmes.titulo == 'Batman').delete()
session.commit()


#Update
session.query(Filmes).filter(Filmes.genero == 'Drama').update({'ano': 2000})  # todos os filmes com o genero de drama foram para o ano 2000
session.commit()


# Select
data = session.query(Filmes).all()
for filme in data:
    print(f'{filme.titulo}')
# fazer uma "query" para pegar todos os elementos que estiverem no banco,
# relacionado a entidade filmes NOTA: query = consulta
print(data)
# tambem podemos acessar os elementos da query
# print(data[0].titulo)

session.close()
