from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes


class AtoresRepository:

    def select(self):
        with DBConnectionHandler() as db:  # aqui estamos acessando tudo que criamos no "DBConnectionHandler"
            data = db.session.query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                Atores.nome,
                Filmes.genero,
                Filmes.titulo
            ).all()  # esse "db" tá pegando tudo que tem "self"
            return data

# na linha 10 o codigo poderia estar mais simplis caso não fosse utilizado o "join"
# db.session.query(Atores, Filmes).with_entities(Atores.nome, Filmes.genero).all()

# perceba q estamos importando as intidades de atores e filmes
