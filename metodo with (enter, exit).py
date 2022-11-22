class OlaMundo:

    def __enter__(self):
        print('Estou entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('estou saindo')


with OlaMundo() as ola:
    print('estou aqui no meio')


# repare que essa estrutura tem uma arranjo de sequencia interessante
# pelo 'enter' e o 'exit'