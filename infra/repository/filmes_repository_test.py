from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock  # essa classe vai possibilitar montar um banco de dados virtual
from infra.entities.filmes import Filmes  # a intidade do banco de dados

session = UnifiedAlchemyMagicMock(  # esses dados são VIRTUAIS
    data=[                          # eles vão auxiliar para os testes
        (
            [  # essa lista vai apresentar uma condição para acessar a lista filmes abaixo
                mock.call.query(Filmes),  # essa aqui é como se fosse a primeira condição
                mock.call.filer(Filmes.genero == 'MMM')  # mais uma condição para acessar o dado
            ],
            [Filmes(titulo='ola', genero='MMM', ano=12)]
        )
    ]
)


def test_select():
    response = session.query(Filmes).filter(Filmes.genero == 'MMM').all()
    print('teste é essa aqui')
    print(response)
