from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

# repo.insert('star wars', 'ficao', 1977)

data = repo.select()

print(data)
