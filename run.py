from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository


repo = AtoresRepository()
response = repo.select()
# print(response)


repo2 = FilmesRepository()
response2 = repo2.select()
filme = response2[0]
print(filme.titulo)
print(filme.atores)
